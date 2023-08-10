# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:08:30 2022

@author: Linus Engstam

Overall model description provided in the following article in Energy Conversion and Management:
"Grid-supported electrolytic hydrogen production: Cost and climate impact using dynamic emission factors"
(https://doi.org/10.1016/j.enconman.2023.117458)
"""

import logging

import numpy as np
import pandas as pd

#from elmada import exceptions
from elmada import helper as hp
from elmada import mappings as mp
from elmada import paths
from elmada import main
from elmada import from_entsoe

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARN)


#Present version details
#can write "overwrite_carbon_tax" to include a specific ETS price

#trading data not included for all neighbouring countries if the 
#main country is not SE

#GB does not have a full dataset for 2021, using 2019 instead

#Transmission capacity limitation implemented
#The idea here is that if we're importing or exporting at maximum capacity
#of the lines, a change in demand in SE will not change the trade to this
#country and it can not provide the marginal source of power.
#A limit of within 1 % of the capacity from Nord Pool is used for safety 
#As the capacity is not known outside of Nord Pool, a limit of 5 % was set if 
#the analyzed country is not SE.

#When the oil-fired plants in SE are in use they are now the source of marginal
#power in the model. 

#Changes to original elmada
#:added SE1-4 to mappings.py
#:added SE fuels to RES in mappings.py
#:slight edit in from_opsd.py to allow for no residual capacity
#:removed NO, CH, EE and LV from mp.EXCLUDED as they will be used
#:removed nuclear as a residual fuel in mappings + skipped nuclear from
# discretize_merit_order_per_fuel in eu_pwl
#:updated gas prices to include 2021 values
#:inlcuded emissions from energy sources not in residual mix in get_CEFs_from_merit_order in from_opsd.py
#:entered NO CC_share in  get_cc_share (eu_pwl) based on Papageorgiou data (https://doi.org/10.1016/j.apenergy.2020.114981)
#in from_other.py (get_ETS_prices) I added the ICE value for 2021 to avoid live mode when not needed otherwise
#:made waste a separate generation type and added emissions to it
#:moved pumped hydro to to non-residual load

def get_emissions_trade(
    year: int,
    ef_type: str, #"AEFs"/"MEFs"/"both"
    country: str = "SE3",
    all_countries: str = "No",
    import_fraction: str = "No",
    **mo_kwargs,
) -> pd.DataFrame:
    """Returns a dataframe with AEFs or MEFs from the specified country and year"""

    #fixed inputs
    freq = "60min"
    cache = False
    use_datetime = False
    
    #Generation capacity data from energiföretagen (see https://doi.org/10.1016/j.enconman.2023.117458)
    #Also some individual plants from ENTSO-E
    
    if year == 2020:
        hours = 8784
    else:
        hours = 8760
    
    #determine neighbouring zones for trading
    C = [country]
    CB = []
    C_excl = []
    if country == "SE1" or country == "SE2" or country == "SE3" or country == "SE4":
        C.extend(["NO", "DK", "FI", "DE", "PL", "LT"])
    else:
        C.extend(mp.NEIGHBOURS_CY.get(country))
        #removing countries with no data from main analysis
        for q in range(len(C)):
            if bool(C[q] in mp.EXCLUDED) is True:
                C_excl.append(C[q]) 

        for w in range(len(C_excl)):
            C.remove(C_excl[w])
            CB.extend([C_excl[w]])

    if country == "SE1":# or bool("SE1" in C) is True:
        C.extend(["SE2", "SE3", "SE4"])
    elif country == "SE2":# or bool("SE2" in C) is True:
        C.extend(["SE1", "SE3", "SE4"])
    elif country == "SE3":# or bool("SE3" in C) is True:
        C.extend(["SE1", "SE2", "SE4"])
    elif country == "SE4":# or bool("SE1" in C) is True:
        C.extend(["SE1", "SE2", "SE3"])
        
    if country != "SE1" and country != "SE2" and  country != "SE3" and country != "SE4":
        if bool("SE1" in C) is True and bool("SE3" in C) is True and bool("SE2" in C) is False:
            C.extend(["SE2", "SE4"])
            #FI
        elif bool("SE2" in C) is True and bool("SE1" in C) is True and bool("SE3" in C) is True:
            C.extend(["SE4"])
            #NO
        elif bool("SE3" in C) is True and bool("SE4" in C) is True:
            C.extend(["SE1", "SE2"])
            #DK
        elif bool("SE4" in C) is True:
            C.extend(["SE1", "SE2", "SE3"])
            #others
        
        #C = list(set(C)) #removing potential doubles
      
    #determine boundary neighbours
    #make sure all neighbouring countries are included
    #otherwise, use assumed constant values from them?
    for i in range(len(C)-1):
       CB_new = [item for item in mp.NEIGHBOURS_CY.get(C[i+1]) if item not in C]
       CB.extend(CB_new)
       CB = list(set(CB)) #removing doubles
            
    #determine individual country internal AEFs
    C_tot = C + CB #all countries analyzed
    C_AEFs = []
    for i in range(len(C_tot)):
        if C_tot[i] == "RU": #no data for this country   
            RU_AEFs = [386]*hours
            RU_AEFs = pd.Series(RU_AEFs)
            RU_AEFs.name = "RU"
            C_AEFs.append(RU_AEFs)
            
        elif C_tot[i] == "MT": #no data for this country
            MT_AEFs = [126]*hours #from EU directive
            MT_AEFs = pd.Series(MT_AEFs)
            MT_AEFs.name = "MT"
            C_AEFs.append(MT_AEFs)
            
        elif C_tot[i] == "UA": #no data for this country
            UA_AEFs = [334]*hours
            UA_AEFs = pd.Series(UA_AEFs)
            UA_AEFs.name = "UA"
            C_AEFs.append(UA_AEFs)
            
        elif C_tot[i] == "SK" and year != 2018 and year != 2019 : #no data for this country
            SK_AEFs = [54]*hours #from EU directive
            SK_AEFs = pd.Series(SK_AEFs)
            SK_AEFs.name = "SK"
            C_AEFs.append(SK_AEFs)
            
        elif C_tot[i] == "BY": #no data for this country
            BY_AEFs = [526]*hours
            BY_AEFs = pd.Series(BY_AEFs)
            BY_AEFs.name = "BY"
            C_AEFs.append(BY_AEFs)
            
        elif C_tot[i] == "LU": #no data for this country
            LU_AEFs = [22]*hours #from EU directive
            LU_AEFs = pd.Series(LU_AEFs)
            LU_AEFs.name = "LU"
            C_AEFs.append(LU_AEFs)
            
        else:
            print(C_tot[i])
            if C_tot[i] == "SE4":
                C_AEFs.append(main.get_emissions(year=year, country=C_tot[i], method="XEF_EP", freq=freq, use_datetime=use_datetime, cache=cache, **mo_kwargs))
            elif C_tot[i] == "GB" and year == 2021:
                C_AEFs.append(main.get_emissions(year=2019, country=C_tot[i], method="XEF_EP", freq=freq, use_datetime=use_datetime, cache=cache, **mo_kwargs))
            else:
                C_AEFs.append(main.get_emissions(year=year, country=C_tot[i], method="XEF_EP", freq=freq, use_datetime=use_datetime, cache=cache, **mo_kwargs))
    
    #determine production data
    C_load = []
    C_load_2021 = []
    for i in range(len(C)):
        if bool(C[i] in mp.COUNTRIES_FOR_ANALYSIS) is True:
            C_load.append(from_entsoe.load_el_national_generation(
                year=year, country=C[i], freq=freq).sum(axis=1))
        else:
            C_load.append(pd.Series([0]*hours))

    #determine trading data
    C_trading = []
    C_no_trade = []
    for i in range(len(C)):
        if bool(C[i] in mp.COUNTRIES_TRADING) is True:
        #The idea is to "read" the headline to determine which country
        #we are trading with without having to individually look at each file
            fp = paths.mode_dependent_cache_dir() / f"{year}_{C[i]}_trade.parquet"
            C_trading.append(hp.read(fp, squeeze=False))
            C_no_trade.extend([0]) #variable to remeber which countries have data
        else:
            C_trading.append(pd.DataFrame(np.zeros((hours, 2))))
            C_no_trade.extend([1])
            logger.warning(f"{C[i]} does not have trading data available.")
    
    C_int_load = []
    #determine total internal load in area, C_load + sum(imports)
    for i in range(len(C)):
        C_int_load.append(C_load[i] + C_trading[i][C_trading[i]>0].sum(axis=1))

        
    #determining non-SE imports to SE zones
    if country == "SE1" or country == "SE2" or country == "SE3" or country == "SE4":
        se1_imp =  C_trading[C.index("SE1")][(C_trading[C.index("SE1")]>0) & (C_trading[C.index("SE1")].columns!="SE2")].sum(axis=1)
        se2_imp =  C_trading[C.index("SE2")][(C_trading[C.index("SE2")]>0) & (C_trading[C.index("SE2")].columns!="SE1") & (C_trading[C.index("SE2")].columns!="SE3")].sum(axis=1)
        se3_imp =  C_trading[C.index("SE3")][(C_trading[C.index("SE3")]>0) & (C_trading[C.index("SE3")].columns!="SE2") & (C_trading[C.index("SE3")].columns!="SE4")].sum(axis=1)
        se4_imp =  C_trading[C.index("SE4")][(C_trading[C.index("SE4")]>0) & (C_trading[C.index("SE4")].columns!="SE3")].sum(axis=1)

    #Set up linear equation system for trading
    #(not sure about the type of all variables...)
    ALL_AEFs = []
    AEFs = []
    for h in range(hours):
        b_int = []
        b_imp = []
        #Vector containing all constant values, i.e with fixed AEFs
        #for each non-boundary country
        for i in range(len(C)):
            b_int += [-C_load[i][h]*C_AEFs[i][h]] #internal generation * internal AEF
            #add the traded load*EF for every country not in C but in CB
            imp = 0
            #looking at every country traded with
            for c in range(C_trading[i].shape[1]):
                if bool(C_trading[i].columns[c] in CB) is True:
                    imp = imp + sum([-max(0,C_trading[i].iloc[h,c])*(C_AEFs[C_tot.index(C_trading[i].columns[c])][h])])
            b_imp += list([imp])
            
        b_int = np.array(b_int)
        b_imp = np.array(b_imp)
        b = np.add(b_int, b_imp)
        
        #define trading system matrix
        #need to implement what happens when a country does not have trading data
        TRADE = []
        for u in range(len(C)):
            TRADE_new = []
            for v in range(len(C)):
                if bool(C[v] in C[u]) is False:
                    if C_no_trade[u] == 0 and bool(C[v] in C_trading[u]) is True:
                        TRADE_new.extend([max(0,C_trading[u].iloc[h,C_trading[u].columns.get_loc(C[v])])])
                    else:
                        TRADE_new.extend([0])
                else:
                    TRADE_new.extend([-C_int_load[u][h]])
            #shape of this?
            TRADE.append(TRADE_new)
        
        #Computes the exact solution, x, of the well-determined linear matrix equation ax = b.
        ALL_AEFs.append(np.linalg.solve(TRADE,b))
        AEFs.append(ALL_AEFs[h][0])
    ALL_AEFs = pd.DataFrame(ALL_AEFs, columns = C)
    #ALL_AEFs = np.array(ALL_AEFs)
    AEFs = pd.Series(AEFs, name=C[0])
    
    if ef_type == "AEFs" or ef_type == "AEF" or ef_type == "AEF" or ef_type == "AEFs": #should maybe move this up to where ALL_AEFs is defined?
        if all_countries == "Yes" or all_countries == "yes":
            return ALL_AEFs
        elif all_countries != "Yes" and all_countries != "yes" and (import_fraction == "Yes" or import_fraction == "yes"):
            if country == "SE1" or country == "SE2" or country == "SE3" or country == "SE4":
                IMPs = []
                for h in range(hours):
                    b_imports = np.array([-se1_imp[h], -se2_imp[h], -se3_imp[h], -se4_imp[h]])
                    IMP = np.array([[-C_int_load[C.index("SE1")][h], max(0,C_trading[C.index("SE1")].iloc[h,C_trading[C.index("SE1")].columns.get_loc("SE2")]), 0, 0],
                                   [max(0,C_trading[C.index("SE2")].iloc[h,C_trading[C.index("SE2")].columns.get_loc("SE1")]), -C_int_load[C.index("SE2")][h], max(0,C_trading[C.index("SE2")].iloc[h,C_trading[C.index("SE2")].columns.get_loc("SE3")]), 0],
                                   [0, max(0,C_trading[C.index("SE3")].iloc[h,C_trading[C.index("SE3")].columns.get_loc("SE2")]), -C_int_load[C.index("SE3")][h], max(0,C_trading[C.index("SE3")].iloc[h,C_trading[C.index("SE3")].columns.get_loc("SE4")])],
                                   [0, 0, max(0,C_trading[C.index("SE4")].iloc[h,C_trading[C.index("SE4")].columns.get_loc("SE3")]), -C_int_load[C.index("SE4")][h]]])
                    IMPs.append(np.linalg.solve(IMP,b_imports))
                IMPs = pd.DataFrame(IMPs, columns=['SE1', 'SE2', 'SE3', 'SE4'])
                IMP_SE1 = (IMPs["SE1"] * C_int_load[C.index("SE1")]).sum() / C_int_load[C.index("SE1")].sum()
                IMP_SE2 = (IMPs["SE2"] * C_int_load[C.index("SE2")]).sum() / C_int_load[C.index("SE2")].sum()
                IMP_SE3 = (IMPs["SE3"] * C_int_load[C.index("SE3")]).sum() / C_int_load[C.index("SE3")].sum()
                IMP_SE4 = (IMPs["SE4"] * C_int_load[C.index("SE4")]).sum() / C_int_load[C.index("SE4")].sum()
                Yearly_IMPs = pd.Series([IMP_SE1, IMP_SE2, IMP_SE3, IMP_SE4], index=["SE1", "SE2", "SE3", "SE4"])
                
                return Yearly_IMPs
            else:
                return ALL_AEFs
                logger.warning("Import fraction is only available for SE zones, returning AEFs for all analyzed countries")
        else:
            return AEFs
    elif ef_type == "MEFs" or ef_type == "MEF" or ef_type == "both" or ef_type == "Both":
        #MEF determination
        #import MEFs for each country
        C_MEFs = []
        C_MC = []
        C_ALL = []
        C_FUEL = []
        C_EP = []
        for i in range(len(C)):
            C_ALL = main.get_emissions(year=year, country=C[i], method="_PWL", freq=freq, use_datetime=use_datetime, cache=cache, **mo_kwargs)
            C_MEFs.append(C_ALL.iloc[:,5])
            C_MC.append(C_ALL.iloc[:,4])
            C_FUEL.append(C_ALL.iloc[:,2])
            #C_EP.append(main.get_prices(year=year, country=C[i], freq=freq, method="hist_EP"))
        
        #assume that the maximum power traded between two countries
        #is the transmission capacity
        TRANS_MAX = []
        for c in range(len(C_trading[0].columns)):
            TRANS_MAX.append(0.95*max(abs(C_trading[0].iloc[:,c])))
            #removing 5 % of the actual maximum as the theoretical maximum capacity is sometimes exceeded
                
        #ALL_MEFs = []
        MEFs = []
        MEF_COST = []
        MEF_SOURCE = []
        MEF_FUEL = []
        se3_4_imp_lim = []
        se3_4_exp_lim = []
        se3_2_imp_lim = []
        se3_2_exp_lim = []
        se1_2_imp_lim = []
        se1_2_exp_lim = []
        
        if country == "SE1" or country == "SE2" or country == "SE3" or country == "SE4":
        #import transmission capacity data
            C_imp_cap = []
            C_exp_cap = []
            se1 = C.index("SE1")
            se3 = C.index("SE3")
            for u in range(len(C)):                        
                #want the lines to be in the same order as below for simpler analysis
                if C[u] == C[0] or C[u] == C[-3] or C[u] == C[-2] or C[u] == C[-1]: 
                    fp_imp = paths.mode_dependent_cache_dir() / f"{year}_{C[u]}_imp_cap.parquet"
                    fp_exp = paths.mode_dependent_cache_dir() / f"{year}_{C[u]}_exp_cap.parquet"
                    C_imp_cap.append(hp.read(fp_imp, squeeze=False))
                    C_exp_cap.append(hp.read(fp_exp, squeeze=False))
                    
                    #determine intra-SE transmission limitations
                    for t in range(hours):
                        if C[u] == "SE3":
                            #is SE3-->SE4 limited? 1 if limited, 0 if not
                            if C_trading[se3].loc[t,"SE4"] > 0:
                                if C_trading[se3].loc[t,"SE4"] > 0.99*C_imp_cap[-1].loc[t,"SE4"]:
                                    se3_4_imp_lim.append(1)
                                    se3_4_exp_lim.append(0)
                                else:
                                    se3_4_imp_lim.append(0)
                                    se3_4_exp_lim.append(0)
                            elif C_trading[se3].loc[t,"SE4"] < 0:
                                if abs(C_trading[se3].loc[t,"SE4"]) > 0.99*C_exp_cap[-1].loc[t,"SE4"]:
                                    se3_4_exp_lim.append(1)
                                    se3_4_imp_lim.append(0)
                                else:
                                    se3_4_exp_lim.append(0)
                                    se3_4_imp_lim.append(0)
                            else:
                                    se3_4_imp_lim.append(0)
                                    se3_4_exp_lim.append(0)
                                    
                            #is SE3-->SE2 limited? 1 if limited, 0 if not
                            if C_trading[se3].loc[t,"SE2"] > 0:
                                if C_trading[se3].loc[t,"SE2"] > 0.99*C_imp_cap[-1].loc[t,"SE2"]:
                                    se3_2_imp_lim.append(1)
                                    se3_2_exp_lim.append(0)
                                else:
                                    se3_2_imp_lim.append(0)
                                    se3_2_exp_lim.append(0)
                            elif C_trading[se3].loc[t,"SE2"] < 0:
                                if abs(C_trading[se3].loc[t,"SE2"]) > 0.99*C_exp_cap[-1].loc[t,"SE2"]:
                                    se3_2_exp_lim.append(1)
                                    se3_2_imp_lim.append(0)
                                else:
                                    se3_2_exp_lim.append(0)
                                    se3_2_imp_lim.append(0)
                            else:
                                    se3_2_imp_lim.append(0)
                                    se3_2_exp_lim.append(0)
                                    
                        if C[u] == "SE1":
                            #is SE1-->SE2 limited? 1 if limited, 0 if not
                            if C_trading[se1].loc[t,"SE2"] > 0:
                                if C_trading[se1].loc[t,"SE2"] > 0.99*C_imp_cap[-1].loc[t,"SE2"]:
                                    se1_2_imp_lim.append(1)
                                    se1_2_exp_lim.append(0)
                                else:
                                    se1_2_imp_lim.append(0)
                                    se1_2_exp_lim.append(0)
                            elif C_trading[se1].loc[t,"SE2"] < 0:
                                if abs(C_trading[se1].loc[t,"SE2"]) > 0.99*C_exp_cap[-1].loc[t,"SE2"]:
                                    se1_2_exp_lim.append(1)
                                    se1_2_imp_lim.append(0)
                                else:
                                    se1_2_exp_lim.append(0)
                                    se1_2_imp_lim.append(0)
                            else:
                                    se1_2_imp_lim.append(0)
                                    se1_2_exp_lim.append(0)

            
            
            C_imp_cap = pd.concat(C_imp_cap, axis=1)
            C_exp_cap = pd.concat(C_exp_cap, axis=1)
        
            #determine the hours where the SE oil plants are active
            se3_oil_hours = from_entsoe.load_el_national_generation(year=year, 
                                                                country="SE3",
                                                                freq="60min").loc[:,"oil"]
            se4_oil_hours = from_entsoe.load_el_national_generation(year=year, 
                                                                country="SE4",
                                                                freq="60min").loc[:,"oil"]
        
        #import electricity price of main country (for negative price check)
        if country != "SE1" and country != "SE2" and country != "SE3" and country != "SE4":
            C_EP = main.get_prices(year=year, country=country, freq=freq, method="hist_EP")
        else:
            fp = paths.mode_dependent_cache_dir() / f"EP_SE_{year}.parquet"
            EPs = hp.read(fp)
            C_EP = EPs[country]
        
        for h in range(hours):
            #determine which country to take MEF from
            
            #want to find the minimum MC and extract its location/country
            C_mar_cost = []
            for i in range(len(C)):
                C_MAR = 1
                #should first define restrictions and then pick cheapest
                #out of the allowed countries
                #1: can't have a MEF of 0 as I have defined it
                if C_MEFs[i][h] == 0:
                    C_MAR = 0
                                
                #if we are not trading with the country it can not provide marginal power
                if country != "SE1" and country != "SE2" and country != "SE3" and country != "SE4":
                    if bool(C[i] in mp.NEIGHBOURS_CY.get(country)) is True:
                        if C_trading[0].iloc[h,C_trading[0].columns.get_loc(C[i])] == 0: #<= indicates only imports
                            C_MAR = 0
                            #Can we import from a country we are presently exporting to?
                    
                        #if close to maximum transmission capacity
                        #taking abs to include times of maximum export
                        if abs(C_trading[0].iloc[h,C_trading[0].columns.get_loc(C[i])]) >= TRANS_MAX[C_trading[0].columns.get_loc(C[i])]:
                            C_MAR = 0
                      
                        #for SE zones we want to consider national borders instead
                if country == "SE1" or country == "SE2" or country == "SE3" or country == "SE4":
                    
                    #chaning order from -1 --> -3 to -3 --> -1
                    se_trading = ([C_trading[0], C_trading[-3], C_trading[-2], C_trading[-1]])
                    se_trading = pd.concat(se_trading, axis=1)
                    se_index = se_trading.columns.get_loc(C[i])
                    C_MAR1 = []
                    #doing below just because se_index can be either int or array
                    if bool(isinstance(se_index, int)) is False:
                        se_index = np.where(se_index)
                        se_index = se_index[0]
                    
                        for x in range(len(se_index)):
                            if se_trading.iloc[h,se_index[x]] == 0: #<= indicates only imports, == both import and export
                                C_MAR1.append(0)
                            
                            #if importing close to maximum capacity
                            elif se_trading.iloc[h,se_index[x]] > 0 and se_trading.iloc[h,se_index[x]] >= 0.99*C_imp_cap.iloc[h,se_index[x]]:
                                C_MAR1.append(0)
                            
                            #if exporting at max capacity
                            elif se_trading.iloc[h,se_index[x]] < 0 and abs(se_trading.iloc[h,se_index[x]]) >= 0.99*C_exp_cap.iloc[h,se_index[x]]:
                                C_MAR1.append(0)
                            
                            else:
                                #looking into SE transmission on a country basis
                                #here, I determine which trade route is used and look at all transmission from the incoming SE zone to the used SE zone
                                if C[i] == "DK":
                                    #looking at DK-SE3 connection if SE4
                                    if country == "SE4" and x == 1:
                                        if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at DK-SE4 connection if SE3
                                    elif country == "SE3" and x == 1:
                                        if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    elif country == "SE2" and x == 0:
                                        #SE3 comes first, x=0 investigates first DK trade
                                        if se3_2_imp_lim == 1 or se3_2_exp_lim == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    elif country == "SE2" and x == 1:
                                        #SE4 comes second, x=1 investigates second DK trade
                                        if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1 or se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    elif country == "SE1" and x == 0:
                                        #SE3 comes first, x=0 investigates first DK trade
                                        if se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1 or se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    elif country == "SE1" and x == 1:
                                        #SE4 comes second, x=1 investigates second DK trade
                                        #we need to move through all zones, SE4--> SE1 and none can be at max
                                        if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1 or se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1 or se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    else:
                                        C_MAR1.append(1)
                                            
                                elif C[i] == "FI":
                                    #looking at FI-SE1 connection if SE4
                                    #se1 comes first, thus x=0
                                    if country == "SE4" and x == 0:
                                        if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1 or se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1 or se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at FI-SE3 connection if SE4
                                    #se3 comes second, thus x=1
                                    elif country == "SE4" and x == 1:
                                        if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at FI-SE1 connection if SE3
                                    elif country == "SE3" and x == 1:
                                        if se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1 or se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    elif country == "SE2" and x == 0:
                                        #SE1 comes first, x=0 investigates first FI trade
                                        if se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    elif country == "SE2" and x == 1:
                                        #SE3 comes second, x=1 investigates second FI trade
                                        if se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    elif country == "SE1" and x == 1:
                                        #SE3 comes second, x=1 investigates second FI trade
                                        if se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1 or se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    else:
                                        C_MAR1.append(1)
                                            
                                elif C[i] == "NO":
                                    #looking at NO-SE1 connection if SE4
                                    #se1 comes first, thus x=0
                                    if country == "SE4" and x == 0:
                                        if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1 or se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1 or se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at NO-SE2 connection if SE4
                                    #se2 comes second, thus x=1
                                    elif country == "SE4" and x == 1:
                                        if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1 or se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at NO-SE3 connection if SE4
                                    #se3 comes third, thus x=2
                                    elif country == "SE4" and x == 2:
                                        if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at NO-SE1 connection if SE3
                                    #se1 comes second, thus x=1
                                    elif country == "SE3" and x == 1:
                                        if se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1 or se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at NO-SE2 connection if SE3
                                    #se2 comes third, thus x=2
                                    elif country == "SE3" and x == 2:
                                        if se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at NO-SE3 connection if SE2
                                    #se3 comes third, thus x=2
                                    elif country == "SE2" and x == 2:
                                        if se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at NO-SE1 connection if SE2
                                    #se1 comes second, thus x=1
                                    elif country == "SE2" and x == 1:
                                        if se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at NO-SE2 connection if SE1
                                    #se2 comes second, thus x=1
                                    elif country == "SE1" and x == 1:
                                        if se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    #looking at NO-SE3 connection if SE1
                                    #se3 comes third, thus x=2
                                    elif country == "SE1" and x == 2:
                                        if se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1 or se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1:
                                            C_MAR1.append(0)
                                        else:
                                            C_MAR1.append(1)
                                    else:
                                        C_MAR1.append(1)
                                        
                                else:
                                    C_MAR1.append(1)
                                
                    else:
                        if se_trading.iloc[h,se_index] == 0: #<= indicates only imports, == both import and export
                            C_MAR1.append(0)
                            
                        #if importing close to maximum capacity
                        elif se_trading.iloc[h,se_index] > 0 and se_trading.iloc[h,se_index] >= 0.99*C_imp_cap.iloc[h,se_index]:
                            C_MAR1.append(0)
                        
                        #if exporting at max capacity
                        elif se_trading.iloc[h,se_index] < 0 and abs(se_trading.iloc[h,se_index]) >= 0.99*C_exp_cap.iloc[h,se_index]:
                            C_MAR1.append(0)
                            
                        else:
                            C_MAR1.append(1)
                                    
                    #basically, if it is not possible to import extra to any SE
                    #zone from this country, it can not provide marginal power
                    if sum(C_MAR1) == 0:
                        C_MAR = 0
                        
                    #trying to implement SE transmission limitations
                    #need the all lines between country and SE zone to be available
                    if C[i] == "DE" or C[i] == "PL" or C[i] == "LT":
                        if country == "SE3":
                            if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1:
                                C_MAR = 0
                        elif country == "SE2":
                            if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1 or se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1:
                                C_MAR = 0
                        elif country == "SE1":
                            if se3_4_imp_lim[h] == 1 or se3_4_exp_lim[h] == 1 or se3_2_imp_lim[h] == 1 or se3_2_exp_lim[h] == 1 or se1_2_imp_lim[h] == 1 or se1_2_exp_lim[h] == 1:
                                C_MAR = 0
  
                if C_MAR == 1:
                    C_mar_cost.append(C_MC[i][h])
                else:
                    #making marginal cost of unavailable countries high to avoid picking them
                    C_mar_cost.append(1000000)
 
    
            if min(C_mar_cost) > 10000:
                mar_country = 0 #country
            else:
                #picking the cheapest
                mar_country = int(C_mar_cost.index(min(C_mar_cost)))
            
            #however, if SE oil plants are active they provide marginal power
            #need to regard transmission capacity between se regions
            #setting a limit of 10 MW to avoid low outputs not related to load
            if country == "SE3":
                #SE3 is prioritized for these zones
                if se3_oil_hours[h] > 10:
                    mar_country = C.index("SE3")
                    #if there is oil production in SE4 and transmission cap not exceeded
                if se4_oil_hours[h] > 10 and se3_4_imp_lim[h] == 0 and se3_4_exp_lim[h] == 0:
                    mar_country = C.index("SE4")
            
            if country == "SE2":
                #if there is oil production in SE4 and transmission cap not exceeded
                if se4_oil_hours[h] > 10 and se3_4_imp_lim[h] == 0 and se3_4_exp_lim[h] == 0 and se3_2_imp_lim[h] == 0 and se3_2_exp_lim[h] == 0:
                    mar_country = C.index("SE4")
                #but SE3 is prioritized for these zones
                elif se3_oil_hours[h] > 10 and se3_2_imp_lim[h] == 0 and se3_2_exp_lim[h] == 0:
                    mar_country = C.index("SE3")
            
            if country == "SE1":
                #if there is oil production in SE4 and transmission cap not exceeded
                if se4_oil_hours[h] > 10 and se3_4_imp_lim[h] == 0 and se3_4_exp_lim[h] == 0 and se3_2_imp_lim[h] == 0 and se3_2_exp_lim[h] == 0 and se1_2_imp_lim[h] == 0 and se1_2_exp_lim[h] == 0:
                    mar_country = C.index("SE4")
                #but SE3 is prioritized for these zones
                elif se3_oil_hours[h] > 10 and se3_2_imp_lim[h] == 0 and se3_2_exp_lim[h] == 0 and se1_2_imp_lim[h] == 0 and se1_2_exp_lim[h] == 0:
                    mar_country = C.index("SE3")
            
            if country == "SE4":
                #SE4 is prioritized for this zone
                if se4_oil_hours[h] > 10:
                    mar_country = C.index("SE4")
                elif se3_oil_hours[h] > 10 and se3_4_imp_lim[h] == 0 and se3_4_exp_lim[h] == 0:
                    mar_country = C.index("SE3")
            
            #checking whether price is negative, in that case renewables is marginal
            #also including case of only internal MEF available (must have <0 emissions)
            if C_EP[h] <= 0 or (min(C_mar_cost) > 10000 and (country == "SE1" or country == "SE2")):
                MEFs.append(15.6) #assumed to be wind power
                MEF_FUEL.append("renewables")
                MEF_COST.append(0)
                MEF_SOURCE.append("undefined")
            else:
                MEFs.append(C_MEFs[mar_country][h]) #C_MEFs.iloc[h,mar_country]
                MEF_FUEL.append(C_FUEL[mar_country][h])
                MEF_COST.append(C_MC[mar_country][h])
                MEF_SOURCE.append(C[mar_country])
        
        if ef_type == "MEFs" or ef_type == "MEF":
        
            if all_countries == "Yes" or all_countries == "yes":
                return C_MEFs
            else:
                return pd.DataFrame(
                    {'MEF': MEFs,
                     'Fuel': MEF_FUEL,
                     'Marginal cost': MEF_COST,
                     'Source': MEF_SOURCE
                     })
            
        elif ef_type == "both" or ef_type == "Both":
            EFs = pd.DataFrame(
                {'AEFs': AEFs,
                 'MEFs': MEFs
                 })
            return EFs
        
    else:    
        raise ValueError(f"EF Type {ef_type} not implemented.")
        


def get_trading_data(
    year: int,
    freq: str = "60min",
    country: str = "SE3",
    cache: bool = False,
) -> pd.DataFrame:
    """Returns a dataframe withtrading data from the specified country and year"""
    #determine trading data
    hours = 8760
    C_trading = []
    if bool(country in mp.COUNTRIES_TRADING) is True:
    #The idea is to "read" the headline to determine which country
    #we are trading with without having to individually look at each file
        fp = paths.mode_dependent_cache_dir() / f"{year}_{country}_trade.parquet"
        C_trading = hp.read(fp, squeeze=False)
    else:
        C_trading = pd.DataFrame(np.zeros((hours, 2)))
        logger.warning(f"{country} does not have trading data available.")

    return C_trading


def get_transmission_imp(
    year: int,
    freq: str = "60min",
    country: str = "SE3",
    cache: bool = False,
) -> pd.DataFrame:
    """Returns a dataframe withtrading data from the specified country and year"""
    #determine trading data
    hours = 8760
    C_imp_cap = []
    if bool(country in mp.COUNTRIES_TRADING) is True:
    #The idea is to "read" the headline to determine which country
    #we are trading with without having to individually look at each file
        fp_imp = paths.mode_dependent_cache_dir() / f"{year}_{country}_imp_cap.parquet"
        C_imp_cap = hp.read(fp_imp, squeeze=False)
    else:
        C_imp_cap = pd.DataFrame(np.zeros((hours, 2)))
        logger.warning(f"{country} does not have trading data available.")

    return C_imp_cap

def get_transmission_exp(
    year: int,
    freq: str = "60min",
    country: str = "SE3",
    cache: bool = False,
) -> pd.DataFrame:
    """Returns a dataframe withtrading data from the specified country and year"""
    #determine trading data
    hours = 8760
    C_exp_cap = []
    if bool(country in mp.COUNTRIES_TRADING) is True:
    #The idea is to "read" the headline to determine which country
    #we are trading with without having to individually look at each file
        fp_exp = paths.mode_dependent_cache_dir() / f"{year}_{country}_exp_cap.parquet"
        C_exp_cap = hp.read(fp_exp, squeeze=False)
    else:
        C_exp_cap = pd.DataFrame(np.zeros((hours, 2)))
        logger.warning(f"{country} does not have trading data available.")

    return C_exp_cap