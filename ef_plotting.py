# -*- coding: utf-8 -*-
"""
Created on Thu May 5 14:47:04 2022

@author: Linus Engstam
"""

"""This script is used for plotting the EF data"""

import elmada
import elmada.linus_part
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.pyplot import figure
import matplotlib.patches as mpatches
import matplotlib.lines as lines

#%matplotlib qt: for window
#%matplotlib inline: for inline

what = "violin" #violin, bars or countries

if what == "violin":
    efs_total = pd.DataFrame()
    efs_2018 = pd.DataFrame()
    efs_2019 = pd.DataFrame()
    efs_2020 = pd.DataFrame()
    efs_2021 = pd.DataFrame()
    for year in range(2018,2022):

        #EFs
        EFs_SE1 = elmada.linus_part.get_emissions_trade(year=year, country="SE1", freq="60min", ef_type="both")
        EFs_SE2 = elmada.linus_part.get_emissions_trade(year=year, country="SE2", freq="60min", ef_type="both")
        EFs_SE3 = elmada.linus_part.get_emissions_trade(year=year, country="SE3", freq="60min", ef_type="both")
        EFs_SE4 = elmada.linus_part.get_emissions_trade(year=year, country="SE4", freq="60min", ef_type="both")

#XEFs
        SE1_XEF=list(EFs_SE1.loc[:,"XEFs"])
        SE2_XEF=list(EFs_SE2.loc[:,"XEFs"])
        SE3_XEF=list(EFs_SE3.loc[:,"XEFs"])
        SE4_XEF=list(EFs_SE4.loc[:,"XEFs"])

#MEFs
        SE1_MEF=list(EFs_SE1.loc[:,"MEFs"])
        SE2_MEF=list(EFs_SE2.loc[:,"MEFs"])
        SE3_MEF=list(EFs_SE3.loc[:,"MEFs"])
        SE4_MEF=list(EFs_SE4.loc[:,"MEFs"])

        if year == 2018:
            efs_2018["SE1 AEFs"] = SE1_XEF
            efs_2018["SE2 AEFs"] = SE2_XEF
            efs_2018["SE3 AEFs"] = SE3_XEF
            efs_2018["SE4 AEFs"] = SE4_XEF
            efs_2018["SE1 MEFs"] = SE1_MEF
            efs_2018["SE2 MEFs"] = SE2_MEF
            efs_2018["SE3 MEFs"] = SE3_MEF
            efs_2018["SE4 MEFs"] = SE4_MEF
        elif year == 2019:
            efs_2019["SE1 AEFs"] = SE1_XEF
            efs_2019["SE2 AEFs"] = SE2_XEF
            efs_2019["SE3 AEFs"] = SE3_XEF
            efs_2019["SE4 AEFs"] = SE4_XEF
            efs_2019["SE1 MEFs"] = SE1_MEF
            efs_2019["SE2 MEFs"] = SE2_MEF
            efs_2019["SE3 MEFs"] = SE3_MEF
            efs_2019["SE4 MEFs"] = SE4_MEF
        elif year == 2020:
            efs_2020["SE1 AEFs"] = SE1_XEF
            efs_2020["SE2 AEFs"] = SE2_XEF
            efs_2020["SE3 AEFs"] = SE3_XEF
            efs_2020["SE4 AEFs"] = SE4_XEF
            efs_2020["SE1 MEFs"] = SE1_MEF
            efs_2020["SE2 MEFs"] = SE2_MEF
            efs_2020["SE3 MEFs"] = SE3_MEF
            efs_2020["SE4 MEFs"] = SE4_MEF
        elif year == 2021:
            efs_2021["SE1 AEFs"] = SE1_XEF
            efs_2021["SE2 AEFs"] = SE2_XEF
            efs_2021["SE3 AEFs"] = SE3_XEF
            efs_2021["SE4 AEFs"] = SE4_XEF
            efs_2021["SE1 MEFs"] = SE1_MEF
            efs_2021["SE2 MEFs"] = SE2_MEF
            efs_2021["SE3 MEFs"] = SE3_MEF
            efs_2021["SE4 MEFs"] = SE4_MEF
        
        
# #XEFs
# XEFs = elmada.linus_part.get_emissions_trade(year=year, country="SE3", freq="60min", all_countries="yes", ef_type="XEFs")
# SE_XEFs = XEFs.loc[:,["SE1","SE2","SE3","SE4"]]
# #df = pd.DataFrame(0, index=[0], columns=["XEF", "MEF", "Area"])
# SE1_XEF=list((SE_XEFs.loc[:,"SE1"]))
# SE2_XEF=list((SE_XEFs.loc[:,"SE2"]))
# SE3_XEF=list((SE_XEFs.loc[:,"SE3"]))
# SE4_XEF=list((SE_XEFs.loc[:,"SE4"]))

        xef_lst = SE1_XEF
        xef_lst.extend(SE2_XEF)
        xef_lst.extend(SE3_XEF)
        xef_lst.extend(SE4_XEF)

# #MEFs
# SE1_MEF = elmada.linus_part.get_emissions_trade(year=year, country="SE1", freq="60min", all_countries="no", ef_type="MEFs")
# SE2_MEF = elmada.linus_part.get_emissions_trade(year=year, country="SE2", freq="60min", all_countries="no", ef_type="MEFs")
# SE3_MEF = elmada.linus_part.get_emissions_trade(year=year, country="SE3", freq="60min", all_countries="no", ef_type="MEFs")
# SE4_MEF = elmada.linus_part.get_emissions_trade(year=year, country="SE4", freq="60min", all_countries="no", ef_type="MEFs")

# mef_lst = list(SE1_MEF.iloc[:,0])
# mef_lst.extend(list(SE2_MEF.iloc[:,0]))
# mef_lst.extend(list(SE3_MEF.iloc[:,0]))
# mef_lst.extend(list(SE4_MEF.iloc[:,0]))

        mef_lst = SE1_MEF
        mef_lst.extend(SE2_MEF)
        mef_lst.extend(SE3_MEF)
        mef_lst.extend(SE4_MEF)

#areas
#pd.Series(np.squeeze(np.zeros((8760,1))))
        SE1_area = []
        SE2_area = []
        SE3_area = []
        SE4_area = []
        if year != 2020:
            for i in range(8760):
                SE1_area.append("SE1")
                SE2_area.append("SE2")
                SE3_area.append("SE3")
                SE4_area.append("SE4")
        elif year == 2020:
            for i in range(8784):
                SE1_area.append("SE1")
                SE2_area.append("SE2")
                SE3_area.append("SE3")
                SE4_area.append("SE4")
    
    
        area_lst = SE1_area
        area_lst.extend(SE2_area)
        area_lst.extend(SE3_area)
        area_lst.extend(SE4_area)

        efs = pd.DataFrame({'XEFs':xef_lst,
                            'MEFs':mef_lst,
                            'Area':area_lst
                            })

        efs_total = efs_total.append(efs)

    year_2021 = []
    year_2020 = []
    year_2019 = []
    year_2018 = []

    for i in range(8760*4):
        year_2021.append("2021")
        year_2019.append("2019")
        year_2018.append("2018")
    
    for i in range(8784*4): #too short but for testing
        year_2020.append("2020")

    year_lst = year_2018
    year_lst.extend(year_2019)
    year_lst.extend(year_2020)
    year_lst.extend(year_2021)

    efs_total['Year'] = year_lst

    #months
    month_short = []
    for u in range(0,4):
        for i in range(8760):
            if i<=(31*24)-1:
                month_short.append("Jan")
            elif i>(31*24)-1 and i <=(59*24)-1:
                month_short.append("Feb")
            elif i>(59*24)-1 and i <=(90*24)-1:
                month_short.append("Mar")
            elif i>(90*24)-1 and i <=(120*24)-1:
                month_short.append("Apr")
            elif i>(120*24)-1 and i <=(151*24)-1:
                month_short.append("May")
            elif i>(151*24)-1 and i <=(181*24)-1:
                month_short.append("Jun")
            elif i>(181*24)-1 and i <=(212*24)-1:
                month_short.append("Jul")
            elif i>(212*24)-1 and i <=(243*24)-1:
                month_short.append("Aug")
            elif i>(243*24)-1 and i <=(273*24)-1:
                month_short.append("Sep")
            elif i>(273*24)-1 and i <=(304*24)-1:
                month_short.append("Oct")
            elif i>(304*24)-1 and i <=(334*24)-1:
                month_short.append("Nov")
            elif i>(334*24)-1 and i <=(365*24)-1:
                month_short.append("Dec")
    
            
    month_long = []
    for u in range(0,4):
        for i in range(8784):
            if i<=(31*24)-1:
                month_long.append("Jan")
            elif i>(31*24)-1 and i <=(60*24)-1:
                month_long.append("Feb")
            elif i>(60*24)-1 and i <=(91*24)-1:
                month_long.append("Mar")
            elif i>(91*24)-1 and i <=(121*24)-1:
                month_long.append("Apr")
            elif i>(121*24)-1 and i <=(152*24)-1:
                month_long.append("May")
            elif i>(152*24)-1 and i <=(182*24)-1:
                month_long.append("Jun")
            elif i>(182*24)-1 and i <=(213*24)-1:
                month_long.append("Jul")
            elif i>(213*24)-1 and i <=(244*24)-1:
                month_long.append("Aug")
            elif i>(244*24)-1 and i <=(274*24)-1:
                month_long.append("Sep")
            elif i>(274*24)-1 and i <=(305*24)-1:
                month_long.append("Oct")
            elif i>(305*24)-1 and i <=(335*24)-1:
                month_long.append("Nov")
            elif i>(335*24)-1 and i <=(366*24)-1:
                month_long.append("Dec")

    
    months = list(np.copy(month_short))
    months.extend(list(np.copy(month_short)))
    months.extend(list(np.copy(month_long)))
    months.extend(list(np.copy(month_short)))
    
    efs_total['Month'] = months
    
    hours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    hour_short = []
    hour_long = []
    #hour of the day
    for i in range(365):
        hour_short.extend(list(np.copy(hours)))
        hour_short.extend(list(np.copy(hours)))
        hour_short.extend(list(np.copy(hours)))
        hour_short.extend(list(np.copy(hours)))
    for i in range(366):
        hour_long.extend(list(np.copy(hours)))
        hour_long.extend(list(np.copy(hours)))
        hour_long.extend(list(np.copy(hours)))
        hour_long.extend(list(np.copy(hours)))
    
    hour = list(np.copy(hour_short))
    hour.extend(list(np.copy(hour_short)))
    hour.extend(list(np.copy(hour_long)))
    hour.extend(list(np.copy(hour_short)))    

    efs_total['Hour'] = hour

    #use this for making more clear box plots
    #https://stackoverflow.com/questions/68614447/how-to-display-boxplot-in-front-of-violinplot-in-seaborn-seaborn-zorder

    mainfont = {'fontname':'Arial'}
    #plotting
    #palettes: Set2, viridis, GnBu_r, BrBG_r, muted, Pastel1
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    f, (ax1, ax2) = plt.subplots(1,2, sharey=True, dpi=500, figsize=(3.54331,1.5), gridspec_kw={'wspace':0.15, 'width_ratios': [4, 1]})
    ax1.set_xlim(0,201)
    ax2.set_xlim(500,551)
    sns.despine(ax=ax1)
    sns.despine(ax=ax2, bottom=True)
    d = 0.015
    kwargs = dict(transform=ax2.transAxes, color='lightgrey', clip_on=False)
    ax2.plot((-d*4, +d*4), (-d, +d), lw=0.2, **kwargs)        # top-left diagonal
    kwargs.update(transform=ax1.transAxes)  # switch to the bottom axes
    ax1.plot((1-d, 1+d), (-d, d), lw=0.2, **kwargs)  # bottom-left diagonal
    ax1.set_xticks([0,50,100,150,200])#, **font)
    #ax1.set_yticks(['SE1', 'SE2', 'SE3'],fontsize=6)#, **font
    ax2.set_xticks([500,550])#, **font)
    ax1.tick_params(axis='both', which='major', labelsize=6)
    ax1.tick_params(axis='both', which='minor', labelsize=6)
    ax2.tick_params(axis='both', which='major', labelsize=6)
    ax2.tick_params(axis='both', which='minor', labelsize=6)
    #ax2.set_yticks(['SE4'],fontsize=6)#, **font
    pal = sns.color_palette("crest",4) #Pastel1
    #Total
    # xef_total = sns.violinplot(ax=ax1, cut=0, x="XEFs", y="Area", data=efs_total, bw=0.2, width=0.9, palette=pal, legend=False, order=['SE1','SE2','SE3','SE4'], linewidth=0.3)
    # xef_se4 = sns.violinplot(ax=ax2, cut=0, x="XEFs", y="Area", data=efs_total, bw=0.2, width=0.9, palette=pal, legend=False, order=['SE1','SE2','SE3','SE4'], linewidth=0.3)
    xef_total = sns.violinplot(scale='width', ax=ax1, cut=0, x="XEFs", y="Area", data=efs_total, bw=0.3, width=0.8, palette=pal, legend=False, order=['SE1','SE2','SE3','SE4'], linewidth=0.3, inner=None, zorder=2)
    xef_se4 = sns.violinplot(scale='width', ax=ax2, cut=0, x="XEFs", y="Area", data=efs_total, bw=0.3, width=0.8, palette=pal, legend=False, order=['SE1','SE2','SE3','SE4'], linewidth=0.3, inner=None, zorder=1)
    boxes = sns.boxplot(ax=ax1, data=efs_total, x="XEFs", y="Area", showcaps=False, width=0.1, fliersize=0, boxprops={'facecolor':'k', "zorder":10}, whiskerprops={'linewidth':0.5, "zorder":10, 'color':'k'}, medianprops={'color':'w', 'linewidth':0.5}, zorder=10, color='k')
    #xef_total = sns.boxplot(data=efs_total, x="XEFs", y="Area", order=["SE1", "SE2", "SE3", "SE4"], palette=pal, whis=10)
    #ax1.set_xlim(0,200)
    #ax2.set_xlim(0,600)
    #sns.set(rc={'figure.figsize':(5,1)})
    #sns.set(font_scale=1.5)
    ax1.set_ylabel("")
    ax2.set_ylabel("")
    ax2.set_xlabel("")
    ax1.set_xlabel("")
    #plt.legend(title="Zone", bbox_to_anchor=(1.13,1.05), prop={'size': 20,})
    ax1.grid(linewidth=0.2)
    ax2.grid(linewidth=0.2)
    ax1.grid(axis='y')
    ax2.grid(axis='y')
    for axis in ['top','bottom','left','right']:
        ax1.spines[axis].set_linewidth(0.2)
        ax2.spines[axis].set_linewidth(0.2)
    plt.title('AEF [gCO$_2$eq/kWh]', fontsize=8, x=-1.7, y=-0.3, **mainfont)
    # f.patch.set_edgecolor('lightgrey')  
    # f.patch.set_linewidth('1')
    ax1.add_patch(mpatches.Rectangle((0.0, -0.5005), 250, 4.005, linewidth=0.2, edgecolor='lightgrey', facecolor='None'))
    ax2.add_patch(mpatches.Rectangle((0.0, -0.5), 550, 3.995, linewidth=0.2, edgecolor='lightgrey', facecolor='None'))
    
    plt.show()
    
    mainfont = {'fontname':'Arial'}
    #plotting
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    f, (ax1) = plt.subplots(dpi=500, figsize=(3.54331,1.5))
    ax1.set_xlim(0,1400)
    #ax1.set_yticks(['SE1', 'SE2', 'SE3'],fontsize=6)#, **font
    ax1.tick_params(axis='both', which='major', labelsize=6)
    ax1.tick_params(axis='both', which='minor', labelsize=6)
    #ax2.set_yticks(['SE4'],fontsize=6)#, **font
    pal = sns.color_palette("flare",4) #Pastel1
    #Total
    xef_total = sns.violinplot(ax=ax1, cut=0, x="MEFs", y="Area", data=efs_total, bw=0.1, width=0.9, palette=pal, legend=False, order=['SE1','SE2','SE3', 'SE4'], linewidth=0.3, inner=None, zorder=1)
    boxes = sns.boxplot(ax=ax1, data=efs_total, x="MEFs", y="Area", showcaps=False, width=0.05, fliersize=0, boxprops={'facecolor':'k', "zorder":10}, whiskerprops={'linewidth':0.5, "zorder":10, 'color':'k'}, medianprops={'color':'w', 'linewidth':0.5}, zorder=10, color='k')
    ax1.set_ylabel("")
    ax1.set_xlabel("MEF [gCO$_2$eq/kWh]", fontsize=8, **mainfont)
    #plt.legend(title="Zone", bbox_to_anchor=(1.13,1.05), prop={'size': 20,})
    ax1.grid(linewidth=0.2)
    ax1.grid(axis='y')
    for axis in ['top','bottom','left','right']:
        ax1.spines[axis].set_linewidth(0.2)
    #plt.title('MEF [g$_{CO_2eq}$/kWh]', fontsize=8, x=-0.1, y=0.5, **mainfont)
    plt.show()
    
    # plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    # params = {'mathtext.default': 'regular' }          
    # plt.rcParams.update(params)
    # plt.xticks(fontsize=6)#, **font)
    # plt.yticks(fontsize=8)#, **font
    # pal = sns.color_palette("flare",4) #Pastel1
    # #Total
    # xef_total = sns.violinplot(cut=0, x="MEFs", y="Area", data=efs_total, bw=0.2, width=0.9, palette=pal, legend=False, order=['SE1','SE2','SE3','SE4'])
    # #xef_total = sns.boxplot(data=efs_total, x="XEFs", y="Area", order=["SE1", "SE2", "SE3", "SE4"], palette=pal, whis=10)
    # plt.xlim(0,1200)
    # #sns.set(rc={'figure.figsize':(5,1)})
    # #sns.set(font_scale=1.5)
    # xef_total.set_ylabel("")
    # xef_total.set_xlabel("MEF [g$_{CO_2eq}$/kWh]", fontsize=8)
    # plt.legend(title="Zone", bbox_to_anchor=(1.13,1.05), prop={'size': 20,})
    # plt.show()
    
    #Annual
    #XEF plots
    #xefs = sns.FacetGrid(efs_total, col="Year",height=5, aspect=10)
    #xefs.map(sns.violinplot, "Area", "XEFs")
    #sns.violinplot(x=efs['Area'], y=efs['XEFs'], bw=0.05, palette=pal)
    #g = sns.catplot(x="Year", y="XEFs", hue="Area", data=efs_total, kind="violin")
    mainfont = {'fontname':'Arial'}
    #plotting
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    f, (ax1) = plt.subplots(dpi=500, figsize=(2*3.54331,2*1.2))
    ax1.grid(linewidth=1.5*0.2)
    ax2.grid(linewidth=1.5*0.2)
    for axis in ['top','bottom','left','right']:
        ax1.spines[axis].set_linewidth(2*0.2)
    plt.xticks(fontsize=1.5*6)#, **font)
    plt.yticks(fontsize=1.5*5)#, **font
    pal = sns.color_palette("crest") #Pastel1
    xef_year = sns.violinplot(linewidth=2*0.3, cut=0, x="Area", y="XEFs", hue="Year", data=efs_total, bw=0.1, width=0.8, palette=pal, height=1, aspect=7, legend=False, order=['SE1','SE2','SE3','SE4'])
    plt.ylim(0,300)
    plt.yticks([0,50,100,150,200,250,300])
    #sns.set(rc={'figure.figsize':(5,1)})
    #sns.set(font_scale=1.5)
    xef_year.set_xlabel("")
    xef_year.set_ylabel("AEF [gCO$_2$eq/kWh]", fontsize=1.5*6)
    plt.legend(bbox_to_anchor=(1.15,1.05), prop={'size': 1.5*5,})
    plt.show()
    #could cut off y-axis and mention that SE4 goes higher?
    #might need to change bw back and forth if figure is weird
    #move legend to the right
    mainfont = {'fontname':'Arial'}
    #plotting
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    f, (ax1) = plt.subplots(dpi=500, figsize=(2*3.54331,2*1.2))
    ax1.grid(linewidth=1.5*0.2)
    ax2.grid(linewidth=1.5*0.2)
    for axis in ['top','bottom','left','right']:
        ax1.spines[axis].set_linewidth(2*0.2)
    plt.xticks(fontsize=1.5*6)#, **font)
    plt.yticks(fontsize=1.5*5)#, **font
    pal = sns.color_palette("flare") #Pastel1
    mef_year = sns.violinplot(linewidth=2*0.3, cut=0, x="Area", y="MEFs", hue="Year", data=efs_total, bw=0.1, width=0.8, palette=pal, height=1, aspect=7, legend=False, order=['SE1','SE2','SE3','SE4'])
    plt.ylim(0,1400)
    plt.yticks([0,200,400,600,800,1000,1200,1400])
    #sns.set(font_scale=1.5)
    mef_year.set_xlabel("")
    mef_year.set_ylabel("MEF [gCO$_2$eq/kWh]", fontsize=1.5*6)
    plt.legend(bbox_to_anchor=(1.0,1.05), prop={'size': 1.5*5,})
    plt.show()
    
    #Monthly
    plt.style.use("seaborn-whitegrid")
    pal = sns.color_palette("crest") #Pastel1
    xef_month = sns.violinplot(cut=0, x="Area", y="XEFs", hue="Month", data=efs_total, bw=0.1, width=0.9, palette=pal, height=1, aspect=10, legend=False, order=['SE1','SE2','SE3','SE4'])
    plt.ylim(0,200)
    #sns.set(rc={'figure.figsize':(5,1)})
    sns.set(font_scale=1.5)
    xef_month.set_xlabel("")
    xef_month.set_ylabel("AEF [gCO$_2$eq/kWh]")
    plt.legend(title="Month", bbox_to_anchor=(1.1,1.05), prop={'size': 16,})
    plt.show()
    
    plt.style.use("seaborn-whitegrid")
    pal = sns.color_palette("flare") #Pastel1
    mef_month = sns.violinplot(cut=0, x="Area", y="MEFs", hue="Month", data=efs_total, bw=0.1, width=0.9, palette=pal, height=1, aspect=7, legend=False, order=['SE1','SE2','SE3','SE4'])
    plt.ylim(0,1400)
    #sns.set(rc={'figure.figsize':(5,1)})
    sns.set(font_scale=1.5)
    mef_month.set_xlabel("")
    mef_month.set_ylabel("MEF [gCO$_2$eq/kWh]")
    plt.legend(title="Month", bbox_to_anchor=(1.1,1.05), prop={'size': 16,})
    plt.show()
    
    #Medians
    monthly_median = efs_total.groupby(['Month','Area']).median()
    monthly_median = monthly_median.reindex(index=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], level=0)
    monthly_average = efs_total.groupby(['Month','Area']).mean()
    monthly_average = monthly_average.reindex(index=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], level=0)
    #plt.plot(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], monthly_average.iloc[:,[0,1]])
    #monthly_average.plot(y="XEFs", use_index=True)
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    plt.xticks(fontsize=22)#, **font)
    plt.yticks(fontsize=22)#, **font
    pal = sns.color_palette("crest", 4) #Pastel1
    xef_month = sns.lineplot(x="Month", y="XEFs", hue="Area", data=monthly_median, palette=pal, lw=7, legend=False)
    xef_month = sns.lineplot(x="Month", y="XEFs", hue="Area", data=monthly_average, palette=pal, lw=4, legend=False, ls='--')
    sns.set(font_scale=2)
    xef_month.set_ylabel('AEFs [gCO$_2$eq/kWh]', fontsize=28)
    xef_month.set_xlabel('Month', fontsize=28)
    plt.xlim([0,11])
    plt.yticks([20,40,60,80])
    plt.ylim([0,80])
    #plt.legend(title="Month", bbox_to_anchor=(1.1,1.05), prop={'size': 16,})
    se1_patch = mpatches.Patch(label='SE1', color=pal[0])
    se2_patch = mpatches.Patch(label='SE2', color=pal[1])
    se3_patch = mpatches.Patch(label='SE3', color=pal[2])
    se4_patch = mpatches.Patch(label='SE4', color=pal[3])
    median_patch = lines.Line2D([0], [0], color='k', lw=4, label='Median', ls='-')
    mean_patch = lines.Line2D([0], [0], color='k', lw=4, label='Mean', ls='--')
    #ax.legend(loc='upper right', handles=[mef_patch, aef_patch], prop={'size': 13,}, bbox_to_anchor=[1.03,1])
    plt.legend(handles=[se1_patch, se2_patch, se3_patch, se4_patch, median_patch, mean_patch], prop={'size': 25,}, loc='upper right', bbox_to_anchor=[1.18,1.02])
    plt.show()
    
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    plt.xticks(fontsize=22)#, **font)
    plt.yticks(fontsize=22)#, **font
    pal = sns.color_palette("flare", 4) #Pastel1
    mef_month = sns.lineplot(x="Month", y="MEFs", hue="Area", data=monthly_median, palette=pal, lw=7, legend=False)
    mef_month = sns.lineplot(x="Month", y="MEFs", hue="Area", data=monthly_average, palette=pal, lw=4, legend=False, ls='--')
    sns.set(font_scale=2)
    mef_month.set_ylabel('AEFs [gCO$_2$eq/kWh]', fontsize=28)
    mef_month.set_xlabel('Month', fontsize=28)
    plt.xlim([0,11])
    plt.ylim([860,980])
    plt.yticks([880,900,920,940,960,980])
    #plt.legend(title="Month", bbox_to_anchor=(1.1,1.05), prop={'size': 16,})
    se1_patch = mpatches.Patch(label='SE1', color=pal[0])
    se2_patch = mpatches.Patch(label='SE2', color=pal[1])
    se3_patch = mpatches.Patch(label='SE3', color=pal[2])
    se4_patch = mpatches.Patch(label='SE4', color=pal[3])
    median_patch = lines.Line2D([0], [0], color='k', lw=4, label='Median', ls='-')
    mean_patch = lines.Line2D([0], [0], color='k', lw=4, label='Mean', ls='--')
    #ax.legend(loc='upper right', handles=[mef_patch, aef_patch], prop={'size': 13,}, bbox_to_anchor=[1.03,1])
    plt.legend(handles=[se1_patch, se2_patch, se3_patch, se4_patch, median_patch, mean_patch], prop={'size': 25,}, loc='upper right', bbox_to_anchor=[1.18,1.02])
    plt.show()
    
    #Hourly
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    pal = sns.color_palette("crest") #Pastel1
    xef_hour = sns.violinplot(cut=0, x="Area", y="XEFs", hue="Hour", data=efs_total, bw=0.1, width=0.9, palette=pal, height=1, aspect=7, legend=False, order=['SE1','SE2','SE3','SE4'])
    plt.ylim(0,200)
    #sns.set(rc={'figure.figsize':(5,1)})
    sns.set(font_scale=1.5)
    xef_hour.set_xlabel("")
    xef_hour.set_ylabel("AEF [gCO$_2$eq/kWh]")
    plt.legend(title="Hour", bbox_to_anchor=(1.05,1.02), prop={'size': 8,})
    plt.show()
    
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    pal = sns.color_palette("flare") #Pastel1
    mef_hour = sns.violinplot(cut=0, x="Area", y="MEFs", hue="Hour", data=efs_total, bw=0.1, width=0.9, palette=pal, height=1, aspect=7, legend=False, order=['SE1','SE2','SE3','SE4'])
    plt.ylim(0,1400)
    #sns.set(rc={'figure.figsize':(5,1)})
    sns.set(font_scale=1.5)
    mef_hour.set_xlabel("")
    mef_hour.set_ylabel("MEF [gCO$_2$eq/kWh]")
    plt.legend(title="Hour", bbox_to_anchor=(1.05,1.05), prop={'size': 8,})
    plt.show()
    
    #Medians
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    plt.xticks(fontsize=22)#, **font)
    plt.yticks(fontsize=22)#, **font)
    hourly_median = efs_total.groupby(['Hour','Area']).median()
    #hourly_median = hourly_median.reindex(index=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], level=0)
    hourly_average = efs_total.groupby(['Hour','Area']).mean()
    #hourly_average = hourly_average.reindex(index=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], level=0)
    #plt.plot(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], monthly_average.iloc[:,[0,1]])
    #monthly_average.plot(y="XEFs", use_index=True)
    pal = sns.color_palette("crest", 4) #Pastel1
    xef_hour = sns.lineplot(x="Hour", y="XEFs", hue="Area", data=hourly_median, palette=pal, lw=7, legend=False)
    xef_hour = sns.lineplot(x="Hour", y="XEFs", hue="Area", data=hourly_average, palette=pal, lw=4, legend=False, ls='--')
    #sns.set(font_scale=2)
    xef_hour.set_ylabel('AEFs [gCO$_2$eq/kWh]', fontsize=28)
    xef_hour.set_xlabel('Hour of the day', fontsize=28)
    plt.xlim([0,23])
    plt.xticks([2,4,6,8,10,12,14,16,18,20,22])
    plt.ylim([0,80])
    #plt.legend(title="Month", bbox_to_anchor=(1.1,1.05), prop={'size': 16,})
    se1_patch = mpatches.Patch(label='SE1', color=pal[0])
    se2_patch = mpatches.Patch(label='SE2', color=pal[1])
    se3_patch = mpatches.Patch(label='SE3', color=pal[2])
    se4_patch = mpatches.Patch(label='SE4', color=pal[3])
    median_patch = lines.Line2D([0], [0], color='k', lw=4, label='Median', ls='-')
    mean_patch = lines.Line2D([0], [0], color='k', lw=4, label='Mean', ls='--')
    #ax.legend(loc='upper right', handles=[mef_patch, aef_patch], prop={'size': 13,}, bbox_to_anchor=[1.03,1])
    plt.legend(handles=[se1_patch, se2_patch, se3_patch, se4_patch, median_patch, mean_patch], prop={'size': 25,}, loc='upper right', bbox_to_anchor=[1.18,1.02])
    plt.show()
    
    pal = sns.color_palette("flare", 4) #Pastel1
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    mef_hour = sns.lineplot(x="Hour", y="MEFs", hue="Area", data=hourly_median, palette=pal, lw=7, legend=False)
    mef_hour = sns.lineplot(x="Hour", y="MEFs", hue="Area", data=hourly_average, palette=pal, lw=4, legend=False, ls='--')
    #sns.set(font_scale=5)
    mef_hour.set_ylabel('MEFs [gCO$_2$eq/kWh]', fontsize=28)
    mef_hour.set_xlabel('Hour of the day', fontsize=28)
    plt.xlim([0,23])
    plt.xticks([2,4,6,8,10,12,14,16,18,20,22])
    plt.ylim([880,960])
    plt.xticks(fontsize=22)#, **font)
    plt.yticks(fontsize=22)#, **font)
    #plt.legend(title="Month", bbox_to_anchor=(1.1,1.05), prop={'size': 16,})
    se1_patch = mpatches.Patch(label='SE1', color=pal[0])
    se2_patch = mpatches.Patch(label='SE2', color=pal[1])
    se3_patch = mpatches.Patch(label='SE3', color=pal[2])
    se4_patch = mpatches.Patch(label='SE4', color=pal[3])
    median_patch = lines.Line2D([0], [0], color='k', lw=4, label='Median', ls='-')
    mean_patch = lines.Line2D([0], [0], color='k', lw=4, label='Mean', ls='--')
    #ax.legend(loc='upper right', handles=[mef_patch, aef_patch], prop={'size': 13,}, bbox_to_anchor=[1.03,1])
    plt.legend(handles=[se1_patch, se2_patch, se3_patch, se4_patch, median_patch, mean_patch], prop={'size': 25,}, loc='upper right', bbox_to_anchor=[1.18,1.02])
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    plt.show()
    
    #electricity price dependency
    elspot = []
    elpath = r'C:\Users\enls0001\Anaconda3\Lib\site-packages\P2X_model\Data\elspot prices 2018.xlsx'
    elspot_2018 = pd.read_excel(elpath)
    elspot.extend(elspot_2018["SE1"].tolist())
    elspot.extend(elspot_2018["SE2"].tolist())
    elspot.extend(elspot_2018["SE3"].tolist())
    elspot.extend(elspot_2018["SE4"].tolist())
    elpath = r'C:\Users\enls0001\Anaconda3\Lib\site-packages\P2X_model\Data\elspot prices 2019.xlsx'
    elspot_2019 = pd.read_excel(elpath)
    elspot.extend(elspot_2019["SE1"].tolist())
    elspot.extend(elspot_2019["SE2"].tolist())
    elspot.extend(elspot_2019["SE3"].tolist())
    elspot.extend(elspot_2019["SE4"].tolist())
    elpath = r'C:\Users\enls0001\Anaconda3\Lib\site-packages\P2X_model\Data\elspot prices 2020.xlsx'
    elspot_2020 = pd.read_excel(elpath)
    elspot.extend(elspot_2020["SE1"].tolist())
    elspot.extend(elspot_2020["SE2"].tolist())
    elspot.extend(elspot_2020["SE3"].tolist())
    elspot.extend(elspot_2020["SE4"].tolist())
    elpath = r'C:\Users\enls0001\Anaconda3\Lib\site-packages\P2X_model\Data\elspot prices 2021.xlsx'
    elspot_2021 = pd.read_excel(elpath)
    elspot.extend(elspot_2021["SE1"].tolist())
    elspot.extend(elspot_2021["SE2"].tolist())
    elspot.extend(elspot_2021["SE3"].tolist())
    elspot.extend(elspot_2021["SE4"].tolist())
    elspot_round = [round(x,-1) for x in elspot]
    efs_total['Elspot rounded'] = elspot_round
    efs_total['Elspot'] = elspot
    
    elspot_average = efs_total.groupby('Elspot').mean()
    
    #f, (ax1) = plt.subplots()
    
    fla = sns.color_palette("flare", 4) #Pastel1
    cre = sns.color_palette("crest", 4) #Pastel1
    plt.style.use("seaborn-whitegrid")
    #mef_el = sns.regplot(x="Elspot", y="MEFs", data=efs_total, marker='.', scatter_kws={"alpha":0.2, "color":"indianred"}, ci=10, line_kws={"color": "maroon"})
    #xef_el = sns.regplot(x="Elspot", y="XEFs", data=efs_total, marker='.', scatter_kws={"alpha":0.2, "color":"mediumseagreen"}, ci=10, line_kws={"color": "seagreen"})
    
    mef_el = sns.lmplot(x="Elspot", y="MEFs", col="Area", data=efs_total, palette=fla, ci=100, line_kws={"color": fla[1]}, scatter_kws={'alpha':0.2,'color': fla[0]})
    #xef_el = sns.lmplot(x="Elspot", y="XEFs", col="Area", data=efs_total, palette=cre, ci=100, line_kws={"color": cre[3]}, scatter_kws={'alpha':0.2, 'color':cre[2]})
    params = {'mathtext.default': 'regular' }
    plt.rcParams.update(params)
    #ax1.set_xlabel('Electricity price [€/MWh]', fontsize=28)
    #ax1.set_ylabel('EFs [g$_{CO_2eq}$/kWh]', fontsize=28)
    # plt.ylim(0,1200)
    # plt.xlim(0,650)
    # plt.xticks(fontsize=22)#, **font)
    # plt.yticks(fontsize=22)#, **font)
    # xef_el.set_axis_labels('', '')
    # xef_el.fig.supylabel('AEFs [gCO$_2$eq/kWh]', fontsize=22)
    # xef_el.fig.supxlabel('Elspot [€/MWh]', fontsize=22)
    # #xef_el.fig.ylim(0,1200)
    # xef_el.set(ylim=(0, 600))
    # #xef_el.fig.xlim(0,650)
    # xef_el.set(xlim=(-10, 800))
    #plt.xticks(fontsize=22)#, **font)
    #plt.yticks(fontsize=22)#, **font)
    mef_el.set_axis_labels('', '')
    mef_el.fig.supylabel('MEFs [g$_{CO_2eq}$/kWh]', fontsize=22)
    mef_el.fig.supxlabel('Elspot [€/MWh]', fontsize=22)
    mef_el.set(ylim=(0,1400))
    mef_el.set(xlim=(-10,800))
    #plt.xticks(fontsize=22)#, **font)
    #plt.yticks(fontsize=22)#, **font)
    #aef_patch = mpatches.Patch(color='indianred', label='MEF')
    #mef_patch = mpatches.Patch(color='mediumseagreen', label='AEF')
    #ax.legend(loc='upper right', handles=[mef_patch, aef_patch], prop={'size': 13,}, bbox_to_anchor=[1.03,1])
    #plt.legend(handles=[aef_patch, mef_patch], prop={'size': 25,}, loc='upper right', bbox_to_anchor=[1,1], frameon=True)
    plt.show()
    
    #load dependency
    #font = {'fontname':'monospace'}
    #plt.rcParams["font.family"] = 'sans-serif'
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    load = []
    freq="60min"
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2018, country="SE1", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2018, country="SE2", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2018, country="SE3", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2018, country="SE4", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2019, country="SE1", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2019, country="SE2", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2019, country="SE3", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2019, country="SE4", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2020, country="SE1", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2020, country="SE2", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2020, country="SE3", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2020, country="SE4", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2021, country="SE1", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2021, country="SE2", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2021, country="SE3", freq=freq).sum(axis=1))
    load.extend(elmada.from_entsoe.load_el_national_generation(year=2021, country="SE4", freq=freq).sum(axis=1))
    efs_total['Load'] = load
    
    #mef_load = sns.lmplot(x="Load", y="MEFs", col="Area", data=efs_total, palette=fla, ci=100, line_kws={"color": fla[1]}, scatter_kws={'alpha':0.2, 'color':fla[0]})
    xef_load = sns.lmplot(x="Load", y="XEFs", col="Area", data=efs_total, palette=cre, ci=100, line_kws={"color": cre[3]}, scatter_kws={'alpha':0.2, 'color': cre[2]})
    params = {'mathtext.default': 'regular' }
    plt.rcParams.update(params)
    #ax1.set_xlabel('Electricity price [€/MWh]', fontsize=28)
    #ax1.set_ylabel('EFs [g$_{CO_2eq}$/kWh]', fontsize=28)
    plt.ylim(0,1400)
    plt.xlim(0,14000)
    xef_load.set_axis_labels('', '')
    xef_load.fig.supylabel('AEFs [g$_{CO_2eq}$/kWh]', fontsize=22)
    xef_load.fig.supxlabel('Domestic electricity generation [MWh]', fontsize=22)
    # mef_load.set_axis_labels('', '')
    # mef_load.fig.supylabel('MEFs [gCO$_2$eq/kWh]', fontsize=22)
    # mef_load.fig.supxlabel('Domestic electricity generation [MWh]', fontsize=22)
    # plt.xticks(fontsize=22)#, **font)
    # plt.yticks(fontsize=22)#, **font)
    
    
    # params = {'mathtext.default': 'regular' }          
    # plt.rcParams.update(params)
    # mef_load = sns.regplot(x="Load", y="MEFs", data=efs_total, marker='.', scatter_kws={"alpha":0.2, "color": "indianred"}, ci=50, line_kws={"color": "maroon", "lw":4})
    # xef_load = sns.regplot(x="Load", y="XEFs", data=efs_total, marker='.', scatter_kws={"alpha":0.2, "color": "mediumseagreen"}, ci=50, line_kws={"color": "seagreen", "lw":4})
    # xef_load.set_xlabel('Electricity load [MWh]', fontsize=28)
    # xef_load.set_ylabel('EFs [g$_{CO_2eq}$/kWh]', fontsize=28)
    # plt.ylim(0,1200)
    # plt.xlim(0,14000)
    # plt.xticks(fontsize=22)#, **font)
    # plt.yticks(fontsize=22)#, **font)
    # aef_patch = mpatches.Patch(color='indianred', label='MEF')
    # mef_patch = mpatches.Patch(color='mediumseagreen', label='AEF')
    # #ax.legend(loc='upper right', handles=[mef_patch, aef_patch], prop={'size': 13,}, bbox_to_anchor=[1.03,1])
    # plt.legend(handles=[aef_patch, mef_patch], prop={'size': 25,}, loc='upper right', bbox_to_anchor=[1,1], frameon=True)
    plt.show()
    
    #dynamic Ef comparison
    pal = sns.color_palette("crest", 4) #Pastel1
    x = []
    for i in range(1,100):
        x.append(i)
        
    #PAPER
    #fig, ax1 = plt.subplots()
    scale=140/90
    fig, ax1 = plt.subplots(dpi=500, figsize=(scale*3.54331,1.5*2))
    ax2 = ax1.twinx()
    plt.style.use("seaborn-whitegrid")
    SE4_no_trade = elmada.get_emissions(year=2021, freq="60min", country="SE4", method="XEF_PWL")
    ax2.plot(x,SE4_no_trade[5226:5325], zorder=22, lw=1, color=pal[0])
    ax2.plot(x,SE4_XEF[5226:5325], zorder=21, lw=1, color=pal[2])
    ax2.set_ylim(0,300)
    ax2.set_yticks([0,75,150,225,300])
    ax2.set_xlim(5226,5325)
    ax1.set_xlim([1,99])
    ax2.set_xlim([1,99])
    ax2.set_xticks([25,50,75])
    ax1.set_ylabel('Generation and imports [MW]', fontsize=7*scale)
    ax2.set_ylabel('AEF [gCO$_2$eq/kWh]', fontsize=7*scale)
    ax1.set_xlabel('Hour', fontsize=7*scale)
    #trading
    fp = elmada.paths.mode_dependent_cache_dir() / f"2021_SE4_trade.parquet"
    trading = elmada.helper.read(fp, squeeze=False)
    trading_imp = trading[trading>=0]
    trading_imp = trading_imp.fillna(0)
    trading_exp = trading[trading<0]
    trading_exp = trading_exp.fillna(0)
    trading_sum = trading.sum(axis=1)
    trading_non_se = trading.iloc[:,1:4].sum(axis=1)
    trading_non_se[trading_non_se<0] = 0
    trading_share = (trading_non_se / trading_sum) * 100
    #trading_non_se = trading_non_se.fillna(0)
    se3_imp = trading_imp.iloc[5226:5325,0]
    dk_imp = trading_imp.iloc[5226:5325,1]
    pl_imp = trading_imp.iloc[5226:5325,2]
    lt_imp = trading_imp.iloc[5226:5325,3]
    de_imp = trading_imp.iloc[5226:5325,4]
    se3_exp = trading_exp.iloc[5226:5325,0]
    dk_exp = trading_exp.iloc[5226:5325,1]
    pl_exp = trading_exp.iloc[5226:5325,2]
    lt_exp = trading_exp.iloc[5226:5325,3]
    de_exp = trading_exp.iloc[5226:5325,4]
    
    #internal generation
    fp = elmada.paths.mode_dependent_cache_dir() / f"2021_SE4_gen_entsoe.parquet"
    se4_gen = elmada.helper.read(fp, squeeze=False)
    se4_gen = se4_gen.sum(axis=1)
    se4_int = se4_gen.iloc[5226:5325]

    ax1.plot(x,se4_int, color='0.3', zorder=12, lw=0)
    ax1.fill_between(x, se4_int, color='0.3', zorder=11, lw=0)
    ax1.plot(x,se4_int+se3_imp, color='0.4', zorder=10, lw=0)
    ax1.fill_between(x, se4_int+se3_imp, color='0.4', zorder=9, lw=0)
    ax1.plot(x,se4_int+dk_imp+se3_imp, color='0.55', zorder=8, lw=0)
    ax1.fill_between(x, se4_int+dk_imp+se3_imp, color='0.55', zorder=7, lw=0)
    ax1.plot(x,se4_int+pl_imp+dk_imp+se3_imp, color='0.65', zorder=6, lw=0)
    ax1.fill_between(x, se4_int+pl_imp+dk_imp+se3_imp, color='0.65', zorder=5, lw=0, hatch='/////', edgecolor='0.4')
    ax1.plot(x,se4_int+lt_imp+pl_imp+dk_imp+se3_imp, color='0.75', zorder=4, lw=0)
    ax1.fill_between(x, se4_int+lt_imp+pl_imp+dk_imp+se3_imp, color='0.75', zorder=3, lw=0, hatch='.....', edgecolor='0.5')
    ax1.plot(x, se4_int+de_imp+lt_imp+pl_imp+dk_imp+se3_imp, color='0.9', zorder=2, lw=0)
    ax1.fill_between(x, se4_int+de_imp+lt_imp+pl_imp+dk_imp+se3_imp, color='0.9', zorder=1, lw=0)
    # ax1.plot(x,se1_exp, color='dimgray', zorder=20)
    # ax1.fill_between(x, se1_exp, color='dimgray', zorder=19)
    # ax1.plot(x,dk_exp+se1_exp, color='gray', zorder=18)
    # ax1.fill_between(x, dk_exp+se1_exp, color='gray', zorder=17)
    # ax1.plot(x,pl_exp+dk_exp+se1_exp, color='darkgray', zorder=16)
    # ax1.fill_between(x, pl_exp+dk_exp+se1_exp, color='darkgray', zorder=15)
    # ax1.plot(x,lt_exp+pl_exp+dk_exp+se1_exp, color='silver', zorder=14)
    # ax1.fill_between(x, lt_exp+pl_exp+dk_exp+se1_exp, color='silver', zorder=13)
    # ax1.plot(x, de_exp+lt_exp+pl_exp+dk_exp+se1_exp, color='lightgray', zorder=12)
    # ax1.fill_between(x, de_exp+lt_exp+pl_exp+dk_exp+se1_exp, color='lightgray', zorder=11)
    ax2.grid(False)
    ax1.grid(linewidth=0.2*scale)
    for axis in ['top','bottom','left','right']:
        ax1.spines[axis].set_linewidth(0.2*scale)
        ax2.spines[axis].set_linewidth(0.2)
    ax1.set_ylim(0,4000)
    ax1.set_yticks([0,1000,2000,3000,4000])
    #ax1.set_frame_on(False)
    for label in (ax1.get_xticklabels() + ax1.get_yticklabels()):
        label.set_fontsize(6*scale)
    for label in (ax2.get_xticklabels() + ax2.get_yticklabels()):
        label.set_fontsize(6*scale)
    se4_patch = mpatches.Patch(color='0.3', label='SE4')
    se3_patch = mpatches.Patch(color='0.4', label='SE3')
    dk_patch = mpatches.Patch(color='0.55', label='DK')
    pl_patch = mpatches.Patch(facecolor='0.65', label='PL', hatch='/////', edgecolor='0.4')
    lt_patch = mpatches.Patch(facecolor='0.75', label='LT', hatch='.....', edgecolor='0.5')
    de_patch = mpatches.Patch(color='0.9', label='DE')
    aef_patch = lines.Line2D([0], [0], color=pal[0], lw=1, label='AEF (without imports)')
    trade_patch = lines.Line2D([0], [0], color=pal[2], lw=1, label='AEF (with imports)')
    legend = fig.legend(loc='center',
       handles=[se4_patch, se3_patch, dk_patch, pl_patch, lt_patch, de_patch],
       frameon=False,
       bbox_to_anchor=(0.02, 0.98, 0.95, 0.12), 
       bbox_transform=ax1.transAxes,
       mode='expand', 
       ncol=7, 
       borderaxespad=-.46,
       prop={'size': scale*6,})
    legend1 = fig.legend(loc='center',
       handles=[aef_patch, trade_patch],
       frameon=False,
       bbox_to_anchor=(0.12, 0.98, 0.78, 0.25), 
       bbox_transform=ax1.transAxes,
       mode='expand', 
       ncol=7, 
       borderaxespad=-.46,
       prop={'size': scale*6,})
    plt.show()
    
    #POSTER
    #fig, ax1 = plt.subplots()
    # fig, ax1 = plt.subplots(dpi=300, figsize=(12,6))
    # ax2 = ax1.twinx()
    # plt.style.use("seaborn-whitegrid")
    # SE4_no_trade = elmada.get_emissions(year=2021, freq="60min", country="SE4", method="XEF_PWL")
    # ax2.plot(x,SE4_no_trade[5226:5325], zorder=22, lw=4, color=pal[0])
    # ax2.plot(x,SE4_XEF[5226:5325], zorder=21, lw=4, color=pal[3])
    # ax2.set_ylim(0,300)
    # ax2.set_yticks([0,75,150,225,300])
    # ax2.set_xlim(5226,5325)
    # ax1.set_xlim([1,99])
    # ax2.set_xlim([1,99])
    # ax2.set_xticks([25,50,75])
    # ax1.set_ylabel('Imports [MWh/h]', fontsize=20)
    # ax2.set_ylabel('AEF [g$_{CO_{2}eq}$/kWh]', fontsize=20)
    # ax1.set_xlabel('Hours', fontsize=20)
    # #trading
    # fp = elmada.paths.mode_dependent_cache_dir() / f"2021_SE4_trade.parquet"
    # trading = elmada.helper.read(fp, squeeze=False)
    # trading_imp = trading[trading>=0]
    # trading_imp = trading_imp.fillna(0)
    # trading_exp = trading[trading<0]
    # trading_exp = trading_exp.fillna(0)
    # trading_sum = trading.sum(axis=1)
    # trading_non_se = trading.iloc[:,1:4].sum(axis=1)
    # trading_non_se[trading_non_se<0] = 0
    # trading_share = (trading_non_se / trading_sum) * 100
    # #trading_non_se = trading_non_se.fillna(0)
    # se3_imp = trading_imp.iloc[5226:5325,0]
    # dk_imp = trading_imp.iloc[5226:5325,1]
    # pl_imp = trading_imp.iloc[5226:5325,2]
    # lt_imp = trading_imp.iloc[5226:5325,3]
    # de_imp = trading_imp.iloc[5226:5325,4]
    # se3_exp = trading_exp.iloc[5226:5325,0]
    # dk_exp = trading_exp.iloc[5226:5325,1]
    # pl_exp = trading_exp.iloc[5226:5325,2]
    # lt_exp = trading_exp.iloc[5226:5325,3]
    # de_exp = trading_exp.iloc[5226:5325,4]
    # ax1.plot(x,se3_imp, color='dimgray', zorder=10, lw=0)
    # ax1.fill_between(x, se3_imp, color='dimgray', zorder=9, lw=0)
    # ax1.plot(x,dk_imp+se3_imp, color='gray', zorder=8, lw=0)
    # ax1.fill_between(x, dk_imp+se3_imp, color='gray', zorder=7, lw=0)
    # ax1.plot(x,pl_imp+dk_imp+se3_imp, color='darkgray', zorder=6, lw=0)
    # ax1.fill_between(x, pl_imp+dk_imp+se3_imp, color='darkgray', zorder=5, lw=0)
    # ax1.plot(x,lt_imp+pl_imp+dk_imp+se3_imp, color='silver', zorder=4, lw=0)
    # ax1.fill_between(x, lt_imp+pl_imp+dk_imp+se3_imp, color='silver', zorder=3, lw=0)
    # ax1.plot(x, de_imp+lt_imp+pl_imp+dk_imp+se3_imp, color='lightgray', zorder=2, lw=0)
    # ax1.fill_between(x, de_imp+lt_imp+pl_imp+dk_imp+se3_imp, color='lightgray', zorder=1, lw=0)
    # ax2.grid(False)
    # ax1.grid(linewidth=1)
    # for axis in ['top','bottom','left','right']:
    #     ax1.spines[axis].set_linewidth(1)
    #     ax2.spines[axis].set_linewidth(1)
    # ax1.set_ylim(0,4000)
    # ax1.set_yticks([0,1000,2000,3000,4000])
    # #ax1.set_frame_on(False)
    # for label in (ax1.get_xticklabels() + ax1.get_yticklabels()):
    #     label.set_fontsize(16)
    # for label in (ax2.get_xticklabels() + ax2.get_yticklabels()):
    #     label.set_fontsize(16)
    # se1_patch = mpatches.Patch(color='dimgray', label='SE3')
    # dk_patch = mpatches.Patch(color='gray', label='DK')
    # pl_patch = mpatches.Patch(color='darkgray', label='PL')
    # lt_patch = mpatches.Patch(color='silver', label='LT')
    # de_patch = mpatches.Patch(color='lightgray', label='DE')
    # aef_patch = lines.Line2D([0], [0], color=pal[0], lw=4, label='AEF (without imports)')
    # trade_patch = lines.Line2D([0], [0], color=pal[3], lw=4, label='AEF (with imports)')
    # legend = fig.legend(loc='center',
    #    handles=[se1_patch, dk_patch, pl_patch, lt_patch, de_patch],
    #    frameon=False,
    #    bbox_to_anchor=(0.05, 0.98, 0.91, 0.1), 
    #    bbox_transform=ax1.transAxes,
    #    mode='expand', 
    #    ncol=7, 
    #    borderaxespad=-.46,
    #    prop={'size': 16,})
    # legend1 = fig.legend(loc='center',
    #    handles=[aef_patch, trade_patch],
    #    frameon=False,
    #    bbox_to_anchor=(0.12, 0.98, 0.78, 0.23), 
    #    bbox_transform=ax1.transAxes,
    #    mode='expand', 
    #    ncol=7, 
    #    borderaxespad=-.46,
    #    prop={'size': 16,})
    # plt.show()
    
if what == "bars":
    
    #MEFs
    SE1_MEF_21 = elmada.linus_part.get_emissions_trade(year=2021, country="SE1", freq="60min", all_countries="no", ef_type="MEFs")
    SE2_MEF_21 = elmada.linus_part.get_emissions_trade(year=2021, country="SE2", freq="60min", all_countries="no", ef_type="MEFs")
    SE3_MEF_21 = elmada.linus_part.get_emissions_trade(year=2021, country="SE3", freq="60min", all_countries="no", ef_type="MEFs")
    SE4_MEF_21 = elmada.linus_part.get_emissions_trade(year=2021, country="SE4", freq="60min", all_countries="no", ef_type="MEFs")
    
    SE1_MEF_20 = elmada.linus_part.get_emissions_trade(year=2020, country="SE1", freq="60min", all_countries="no", ef_type="MEFs")
    SE2_MEF_20 = elmada.linus_part.get_emissions_trade(year=2020, country="SE2", freq="60min", all_countries="no", ef_type="MEFs")
    SE3_MEF_20 = elmada.linus_part.get_emissions_trade(year=2020, country="SE3", freq="60min", all_countries="no", ef_type="MEFs")
    SE4_MEF_20 = elmada.linus_part.get_emissions_trade(year=2020, country="SE4", freq="60min", all_countries="no", ef_type="MEFs")

    SE1_MEF_19 = elmada.linus_part.get_emissions_trade(year=2019, country="SE1", freq="60min", all_countries="no", ef_type="MEFs")
    SE2_MEF_19 = elmada.linus_part.get_emissions_trade(year=2019, country="SE2", freq="60min", all_countries="no", ef_type="MEFs")
    SE3_MEF_19 = elmada.linus_part.get_emissions_trade(year=2019, country="SE3", freq="60min", all_countries="no", ef_type="MEFs")
    SE4_MEF_19 = elmada.linus_part.get_emissions_trade(year=2019, country="SE4", freq="60min", all_countries="no", ef_type="MEFs")

    SE1_MEF_18 = elmada.linus_part.get_emissions_trade(year=2018, country="SE1", freq="60min", all_countries="no", ef_type="MEFs")
    SE2_MEF_18 = elmada.linus_part.get_emissions_trade(year=2018, country="SE2", freq="60min", all_countries="no", ef_type="MEFs")
    SE3_MEF_18 = elmada.linus_part.get_emissions_trade(year=2018, country="SE3", freq="60min", all_countries="no", ef_type="MEFs")
    SE4_MEF_18 = elmada.linus_part.get_emissions_trade(year=2018, country="SE4", freq="60min", all_countries="no", ef_type="MEFs")
    
    # SE1_AEF_21 = elmada.linus_part.get_emissions_trade(year=2021, country="SE1", freq="60min", all_countries="no", ef_type="AEFs")
    # SE2_AEF_21 = elmada.linus_part.get_emissions_trade(year=2021, country="SE2", freq="60min", all_countries="no", ef_type="AEFs")
    # SE3_AEF_21 = elmada.linus_part.get_emissions_trade(year=2021, country="SE3", freq="60min", all_countries="no", ef_type="AEFs")
    # SE4_AEF_21 = elmada.linus_part.get_emissions_trade(year=2021, country="SE4", freq="60min", all_countries="no", ef_type="AEFs")
    
    # SE1_AEF_20 = elmada.linus_part.get_emissions_trade(year=2020, country="SE1", freq="60min", all_countries="no", ef_type="AEFs")
    # SE2_AEF_20 = elmada.linus_part.get_emissions_trade(year=2020, country="SE2", freq="60min", all_countries="no", ef_type="AEFs")
    # SE3_AEF_20 = elmada.linus_part.get_emissions_trade(year=2020, country="SE3", freq="60min", all_countries="no", ef_type="AEFs")
    # SE4_AEF_20 = elmada.linus_part.get_emissions_trade(year=2020, country="SE4", freq="60min", all_countries="no", ef_type="AEFs")

    # SE1_AEF_19 = elmada.linus_part.get_emissions_trade(year=2019, country="SE1", freq="60min", all_countries="no", ef_type="AEFs")
    # SE2_AEF_19 = elmada.linus_part.get_emissions_trade(year=2019, country="SE2", freq="60min", all_countries="no", ef_type="AEFs")
    # SE3_AEF_19 = elmada.linus_part.get_emissions_trade(year=2019, country="SE3", freq="60min", all_countries="no", ef_type="AEFs")
    # SE4_AEF_19 = elmada.linus_part.get_emissions_trade(year=2019, country="SE4", freq="60min", all_countries="no", ef_type="AEFs")

    # SE1_AEF_18 = elmada.linus_part.get_emissions_trade(year=2018, country="SE1", freq="60min", all_countries="no", ef_type="AEFs")
    # SE2_AEF_18 = elmada.linus_part.get_emissions_trade(year=2018, country="SE2", freq="60min", all_countries="no", ef_type="AEFs")
    # SE3_AEF_18 = elmada.linus_part.get_emissions_trade(year=2018, country="SE3", freq="60min", all_countries="no", ef_type="AEFs")
    # SE4_AEF_18 = elmada.linus_part.get_emissions_trade(year=2018, country="SE4", freq="60min", all_countries="no", ef_type="AEFs")

    
    c_year_2021 = []
    c_year_2020 = []
    c_year_2019 = []
    c_year_2018 = []
    f_year_2021 = []
    f_year_2020 = []
    f_year_2019 = []
    f_year_2018 = []
    
    for i in range(32):
        c_year_2021.append("2021")
        c_year_2019.append("2019")
        c_year_2018.append("2018")
    
    for i in range(32):
        c_year_2020.append("2020")  
        
    for i in range(24):
        f_year_2021.append("2021")
        f_year_2019.append("2019")
        f_year_2018.append("2018")
    
    for i in range(24):
        f_year_2020.append("2020")
    
    c_zone_1 = []
    c_zone_2 = []
    c_zone_3 = []
    c_zone_4 = []
    f_zone_1 = []
    f_zone_2 = []
    f_zone_3 = []
    f_zone_4 = []
    
    for i in range(8):
        c_zone_1.append('SE1')
        c_zone_2.append('SE2')
        c_zone_3.append('SE3')
        c_zone_4.append('SE4')
        
    for i in range(6):
        f_zone_1.append('SE1')
        f_zone_2.append('SE2')
        f_zone_3.append('SE3')
        f_zone_4.append('SE4')
    
    c_zones = c_zone_1 + c_zone_2 + c_zone_3 + c_zone_4
    f_zones = f_zone_1 + f_zone_2 + f_zone_3 + f_zone_4
    
    # MEF_21['Year'] = year_2021
    #count country frequency
    cty_se1_21 = SE1_MEF_21['Source'].value_counts()# / len(SE1_MEF_21['Source'])
    cty_se2_21 = SE2_MEF_21['Source'].value_counts()# / len(SE2_MEF_21['Source'])
    cty_se3_21 = SE3_MEF_21['Source'].value_counts()# / len(SE3_MEF_21['Source'])
    cty_se4_21 = SE4_MEF_21['Source'].value_counts()# / len(SE4_MEF_21['Source'])
    
    cty_se1_20 = SE1_MEF_20['Source'].value_counts()# / len(SE1_MEF_21['Source'])
    cty_se2_20 = SE2_MEF_20['Source'].value_counts()# / len(SE2_MEF_21['Source'])
    cty_se3_20 = SE3_MEF_20['Source'].value_counts()# / len(SE3_MEF_21['Source'])
    cty_se4_20 = SE4_MEF_20['Source'].value_counts()# / len(SE4_MEF_21['Source'])
    
    cty_se1_19 = SE1_MEF_19['Source'].value_counts()# / len(SE1_MEF_21['Source'])
    cty_se2_19 = SE2_MEF_19['Source'].value_counts()# / len(SE2_MEF_21['Source'])
    cty_se3_19 = SE3_MEF_19['Source'].value_counts()# / len(SE3_MEF_21['Source'])
    cty_se4_19 = SE4_MEF_19['Source'].value_counts()# / len(SE4_MEF_21['Source'])
    
    cty_se1_18 = SE1_MEF_18['Source'].value_counts()# / len(SE1_MEF_21['Source'])
    cty_se2_18 = SE2_MEF_18['Source'].value_counts()# / len(SE2_MEF_21['Source'])
    cty_se3_18 = SE3_MEF_18['Source'].value_counts()# / len(SE3_MEF_21['Source'])
    cty_se4_18 = SE4_MEF_18['Source'].value_counts()# / len(SE4_MEF_21['Source'])
    
    #data handling
    cty_ind = ['SE', 'NO', 'DK', 'FI', 'DE', 'PL', 'LT', 'UNDEF.']
    cty_val_se1_21 = [cty_se1_21['SE3']+cty_se1_21['SE4'], cty_se1_21['NO'], cty_se1_21['DK'], cty_se1_21['FI'], cty_se1_21['DE'], cty_se1_21['PL'], 0, cty_se1_21['undefined']]
    cty_val_se2_21 = [cty_se2_21['SE3']+cty_se2_21['SE4'], cty_se2_21['NO'], cty_se2_21['DK'], cty_se2_21['FI'], cty_se2_21['DE'], cty_se2_21['PL'], 0, cty_se2_21['undefined']]
    cty_val_se3_21 = [cty_se3_21['SE3']+cty_se3_21['SE4'], cty_se3_21['NO'], cty_se3_21['DK'], cty_se3_21['FI'], cty_se3_21['DE'], cty_se3_21['PL'], 0, cty_se3_21['undefined']]
    cty_val_se4_21 = [cty_se4_21['SE3']+cty_se4_21['SE4'], cty_se4_21['NO'], cty_se4_21['DK'], 0, cty_se4_21['DE'], cty_se4_21['PL'], cty_se4_21['LT'], cty_se4_21['undefined']]

    cty_val_se1_20 = [cty_se1_20['SE3']+cty_se1_20['SE4'], cty_se1_20['NO'], cty_se1_20['DK'], cty_se1_20['FI'], cty_se1_20['DE'], cty_se1_20['PL'], 0, cty_se1_20['undefined']]
    cty_val_se2_20 = [cty_se2_20['SE3']+cty_se2_20['SE4'], cty_se2_20['NO'], cty_se2_20['DK'], cty_se2_20['FI'], cty_se2_20['DE'], cty_se2_20['PL'], 0, cty_se2_20['undefined']]
    cty_val_se3_20 = [cty_se3_20['SE3']+cty_se3_20['SE4'], cty_se3_20['NO'], cty_se3_20['DK'], cty_se3_20['FI'], cty_se3_20['DE'], cty_se3_20['PL'], 0, cty_se3_20['undefined']]
    cty_val_se4_20 = [cty_se4_20['SE3']+cty_se4_20['SE4'], cty_se4_20['NO'], cty_se4_20['DK'], cty_se4_20['FI'], cty_se4_20['DE'], cty_se4_20['PL'], 0, cty_se4_20['undefined']]

    cty_val_se1_19 = [cty_se1_19['SE3']+cty_se1_19['SE4'], cty_se1_19['NO'], cty_se1_19['DK'], cty_se1_19['FI'], cty_se1_19['DE'], cty_se1_19['PL'], 0, 0]
    cty_val_se2_19 = [cty_se2_19['SE3']+cty_se2_19['SE4'], cty_se2_19['NO'], cty_se2_19['DK'], cty_se2_19['FI'], cty_se2_19['DE'], cty_se2_19['PL'], 0, 0]
    cty_val_se3_19 = [cty_se3_19['SE3']+cty_se3_19['SE4'], cty_se3_19['NO'], cty_se3_19['DK'], cty_se3_19['FI'], cty_se3_19['DE'], cty_se3_19['PL'], 0, 0]
    cty_val_se4_19 = [cty_se4_19['SE3']+cty_se4_19['SE4'], 0, cty_se4_19['DK'], cty_se4_19['FI'], cty_se4_19['DE'], cty_se4_19['PL'], cty_se4_19['LT'], 0]

    cty_val_se1_18 = [cty_se1_18['SE3']+cty_se1_18['SE4'], cty_se1_18['NO'], cty_se1_18['DK'], cty_se1_18['FI'], cty_se1_18['DE'], cty_se1_18['PL'], cty_se1_18['LT'], 0]
    cty_val_se2_18 = [cty_se2_18['SE3']+cty_se2_18['SE4'], cty_se2_18['NO'], cty_se2_18['DK'], cty_se2_18['FI'], cty_se2_18['DE'], cty_se2_18['PL'], cty_se2_18['LT'], 0]
    cty_val_se3_18 = [cty_se3_18['SE3']+cty_se3_18['SE4'], cty_se3_18['NO'], cty_se3_18['DK'], cty_se3_18['FI'], cty_se3_18['DE'], cty_se3_18['PL'], cty_se3_18['LT'], 0]
    cty_val_se4_18 = [cty_se4_18['SE3']+cty_se4_18['SE4'], 0, cty_se4_18['DK'], cty_se4_18['FI'], cty_se4_18['DE'], cty_se4_18['PL'], cty_se4_18['LT'], 0]


    c_se1_21 = pd.Series(data=cty_val_se1_21, index=cty_ind)
    c_se2_21 = pd.Series(data=cty_val_se2_21, index=cty_ind)
    c_se3_21 = pd.Series(data=cty_val_se3_21, index=cty_ind)
    c_se4_21 = pd.Series(data=cty_val_se4_21, index=cty_ind)
    
    c_se1_20 = pd.Series(data=cty_val_se1_21, index=cty_ind)
    c_se2_20 = pd.Series(data=cty_val_se2_21, index=cty_ind)
    c_se3_20 = pd.Series(data=cty_val_se3_21, index=cty_ind)
    c_se4_20 = pd.Series(data=cty_val_se4_21, index=cty_ind)
    
    c_se1_19 = pd.Series(data=cty_val_se1_21, index=cty_ind)
    c_se2_19 = pd.Series(data=cty_val_se2_21, index=cty_ind)
    c_se3_19 = pd.Series(data=cty_val_se3_21, index=cty_ind)
    c_se4_19 = pd.Series(data=cty_val_se4_21, index=cty_ind)
    
    c_se1_18 = pd.Series(data=cty_val_se1_21, index=cty_ind)
    c_se2_18 = pd.Series(data=cty_val_se2_21, index=cty_ind)
    c_se3_18 = pd.Series(data=cty_val_se3_21, index=cty_ind)
    c_se4_18 = pd.Series(data=cty_val_se4_21, index=cty_ind)

    values_21 = pd.Series()
    values_21 = values_21.append(c_se1_21)
    values_21 = values_21.append(c_se2_21)
    values_21 = values_21.append(c_se3_21)
    values_21 = values_21.append(c_se4_21)
    
    values_20 = pd.Series()
    values_20 = values_20.append(c_se1_20)
    values_20 = values_20.append(c_se2_20)
    values_20 = values_20.append(c_se3_20)
    values_20 = values_20.append(c_se4_20)
    
    values_19 = pd.Series()
    values_19 = values_19.append(c_se1_19)
    values_19 = values_19.append(c_se2_19)
    values_19 = values_19.append(c_se3_19)
    values_19 = values_19.append(c_se4_19)
    
    values_18 = pd.Series()
    values_18 = values_18.append(c_se1_18)
    values_18 = values_18.append(c_se2_18)
    values_18 = values_18.append(c_se3_18)
    values_18 = values_18.append(c_se4_18)
    
    #count fuel frequency
    fuel_se1_21 = SE1_MEF_21['Fuel'].value_counts()# / len(SE1_MEF_21['Fuel'])
    fuel_se2_21 = SE2_MEF_21['Fuel'].value_counts()# / len(SE2_MEF_21['Fuel'])
    fuel_se3_21 = SE3_MEF_21['Fuel'].value_counts()# / len(SE3_MEF_21['Fuel'])
    fuel_se4_21 = SE4_MEF_21['Fuel'].value_counts()# / len(SE4_MEF_21['Fuel'])
    
    fuel_se1_20 = SE1_MEF_20['Fuel'].value_counts()# / len(SE1_MEF_21['Source'])
    fuel_se2_20 = SE2_MEF_20['Fuel'].value_counts()# / len(SE2_MEF_21['Source'])
    fuel_se3_20 = SE3_MEF_20['Fuel'].value_counts()# / len(SE3_MEF_21['Source'])
    fuel_se4_20 = SE4_MEF_20['Fuel'].value_counts()# / len(SE4_MEF_21['Source'])
    
    fuel_se1_19 = SE1_MEF_19['Fuel'].value_counts()# / len(SE1_MEF_21['Source'])
    fuel_se2_19 = SE2_MEF_19['Fuel'].value_counts()# / len(SE2_MEF_21['Source'])
    fuel_se3_19 = SE3_MEF_19['Fuel'].value_counts()# / len(SE3_MEF_21['Source'])
    fuel_se4_19 = SE4_MEF_19['Fuel'].value_counts()# / len(SE4_MEF_21['Source'])
    
    fuel_se1_18 = SE1_MEF_18['Fuel'].value_counts()# / len(SE1_MEF_21['Source'])
    fuel_se2_18 = SE2_MEF_18['Fuel'].value_counts()# / len(SE2_MEF_21['Source'])
    fuel_se3_18 = SE3_MEF_18['Fuel'].value_counts()# / len(SE3_MEF_21['Source'])
    fuel_se4_18 = SE4_MEF_18['Fuel'].value_counts()# / len(SE4_MEF_21['Source'])
    
    fuel_ind = ['coal', 'lignite', 'oil', 'gas_cc', 'gas', 'biomass', 'nuclear', 'renewables',]
    fuel_val_se4_21 = [fuel_se4_21['coal'], fuel_se4_21['lignite'], fuel_se4_21['oil'], fuel_se4_21['gas_cc'], fuel_se4_21['gas'], fuel_se4_21['biomass'], fuel_se4_21['nuclear'], fuel_se4_21['renewables']]
    fuel_val_se2_21 = [fuel_se2_21['coal'], fuel_se2_21['lignite'], fuel_se2_21['oil'], fuel_se2_21['gas_cc'], 0, fuel_se2_21['biomass'], fuel_se2_21['nuclear'], fuel_se2_21['renewables']+fuel_se2_21[0]]
    fuel_val_se3_21 = [fuel_se3_21['coal'], fuel_se3_21['lignite'], fuel_se3_21['oil'], fuel_se3_21['gas_cc'], 0, fuel_se3_21['biomass'], fuel_se3_21['nuclear'], fuel_se3_21['renewables']]
    fuel_val_se1_21 = [fuel_se1_21['coal'], fuel_se1_21['lignite'], fuel_se1_21['oil'], fuel_se1_21['gas_cc'], 0, fuel_se4_21['biomass'], fuel_se4_21['nuclear'], fuel_se1_21['renewables']+fuel_se1_21[0]]

    fuel_val_se4_20 = [fuel_se4_20['coal'], fuel_se4_20['lignite'], fuel_se4_20['oil'], 0, fuel_se4_20['gas'], 0, fuel_se4_20['nuclear'], fuel_se4_20['renewables']]
    fuel_val_se2_20 = [fuel_se2_20['coal'], fuel_se2_20['lignite'], fuel_se2_20['oil'], fuel_se2_20['gas_cc'], fuel_se2_20['gas'], 0, fuel_se2_20['nuclear'], fuel_se2_20['renewables']]
    fuel_val_se3_20 = [fuel_se3_20['coal'], fuel_se3_20['lignite'], fuel_se3_20['oil'], fuel_se3_20['gas_cc'], fuel_se3_20['gas'], 0, fuel_se3_20['nuclear'], fuel_se3_20['renewables']]
    fuel_val_se1_20 = [fuel_se1_20['coal'], fuel_se1_20['lignite'], fuel_se1_20['oil'], fuel_se1_20['gas_cc'], fuel_se1_20['gas'], 0, fuel_se1_20['nuclear'], fuel_se1_20['renewables']]

    fuel_val_se4_19 = [fuel_se4_19['coal'], fuel_se4_19['lignite'], fuel_se4_19['oil'], fuel_se4_19['gas_cc'], fuel_se4_19['gas'], 0, fuel_se4_19['nuclear'], 0]
    fuel_val_se2_19 = [fuel_se2_19['coal'], fuel_se2_19['lignite'], fuel_se2_19['oil'], fuel_se2_19['gas_cc'], fuel_se2_19['gas'], 0, fuel_se2_19['nuclear'], 0]
    fuel_val_se3_19 = [fuel_se3_19['coal'], fuel_se3_19['lignite'], fuel_se3_19['oil'], fuel_se3_19['gas_cc'], fuel_se3_19['gas'], 0, fuel_se3_19['nuclear'], 0]
    fuel_val_se1_19 = [fuel_se1_19['coal'], fuel_se1_19['lignite'], fuel_se1_19['oil'], fuel_se1_19['gas_cc'], fuel_se1_19['gas'], 0, fuel_se1_19['nuclear'], 0]

    fuel_val_se4_18 = [fuel_se4_18['coal'], fuel_se4_18['lignite'], fuel_se4_18['oil'], fuel_se4_18['gas_cc'], fuel_se4_18['gas'], 0, fuel_se4_18['nuclear'], 0]
    fuel_val_se2_18 = [fuel_se2_18['coal'], fuel_se2_18['lignite'], fuel_se2_18['oil'], fuel_se2_18['gas_cc'], fuel_se2_18['gas'], 0, fuel_se2_18['nuclear'], 0]
    fuel_val_se3_18 = [fuel_se3_18['coal'], fuel_se3_18['lignite'], fuel_se3_18['oil'], fuel_se3_18['gas_cc'], fuel_se3_18['gas'], 0, fuel_se3_18['nuclear'], 0]
    fuel_val_se1_18 = [fuel_se1_18['coal'], fuel_se1_18['lignite'], fuel_se1_18['oil'], fuel_se1_18['gas_cc'], fuel_se1_18['gas'], 0, fuel_se1_18['nuclear'], 0]

    f_se1_21 = pd.Series(data=fuel_val_se1_21, index=fuel_ind)
    f_se2_21 = pd.Series(data=fuel_val_se2_21, index=fuel_ind)
    f_se3_21 = pd.Series(data=fuel_val_se3_21, index=fuel_ind)
    f_se4_21 = pd.Series(data=fuel_val_se4_21, index=fuel_ind)
    
    f_se1_20 = pd.Series(data=fuel_val_se1_21, index=fuel_ind)
    f_se2_20 = pd.Series(data=fuel_val_se2_21, index=fuel_ind)
    f_se3_20 = pd.Series(data=fuel_val_se3_21, index=fuel_ind)
    f_se4_20 = pd.Series(data=fuel_val_se4_21, index=fuel_ind)
    
    f_se1_19 = pd.Series(data=fuel_val_se1_21, index=fuel_ind)
    f_se2_19 = pd.Series(data=fuel_val_se2_21, index=fuel_ind)
    f_se3_19 = pd.Series(data=fuel_val_se3_21, index=fuel_ind)
    f_se4_19 = pd.Series(data=fuel_val_se4_21, index=fuel_ind)
    
    f_se1_18 = pd.Series(data=fuel_val_se1_21, index=fuel_ind)
    f_se2_18 = pd.Series(data=fuel_val_se2_21, index=fuel_ind)
    f_se3_18 = pd.Series(data=fuel_val_se3_21, index=fuel_ind)
    f_se4_18 = pd.Series(data=fuel_val_se4_21, index=fuel_ind)
    
    f_values_21 = pd.Series()
    f_values_21 = f_values_21.append(f_se1_21)
    f_values_21 = f_values_21.append(f_se2_21)
    f_values_21 = f_values_21.append(f_se3_21)
    f_values_21 = f_values_21.append(f_se4_21)
    
    f_values_20 = pd.Series()
    f_values_20 = f_values_20.append(f_se1_20)
    f_values_20 = f_values_20.append(f_se2_20)
    f_values_20 = f_values_20.append(f_se3_20)
    f_values_20 = f_values_20.append(f_se4_20)
    
    f_values_19 = pd.Series()
    f_values_19 = f_values_19.append(f_se1_19)
    f_values_19 = f_values_19.append(f_se2_19)
    f_values_19 = f_values_19.append(f_se3_19)
    f_values_19 = f_values_19.append(f_se4_19)
    
    f_values_18 = pd.Series()
    f_values_18 = f_values_18.append(f_se1_18)
    f_values_18 = f_values_18.append(f_se2_18)
    f_values_18 = f_values_18.append(f_se3_18)
    f_values_18 = f_values_18.append(f_se4_18)
    
    #MEF plots
    #countries
    #2021
    
    c_se_21 = [cty_val_se1_21[0], cty_val_se2_21[0], cty_val_se3_21[0], cty_val_se4_21[0]]
    c_no_21 = [cty_val_se1_21[1], cty_val_se2_21[1], cty_val_se3_21[1], cty_val_se4_21[1]]
    c_dk_21 = [cty_val_se1_21[2], cty_val_se2_21[2], cty_val_se3_21[2], cty_val_se4_21[2]]
    c_fi_21 = [cty_val_se1_21[3], cty_val_se2_21[3], cty_val_se3_21[3], cty_val_se4_21[3]]
    c_de_21 = [cty_val_se1_21[4], cty_val_se2_21[4], cty_val_se3_21[4], cty_val_se4_21[4]]
    c_pl_21 = [cty_val_se1_21[5], cty_val_se2_21[5], cty_val_se3_21[5], cty_val_se4_21[5]]
    c_lt_21 = [cty_val_se1_21[6], cty_val_se2_21[6], cty_val_se3_21[6], cty_val_se4_21[6]]
    c_un_21 = [cty_val_se1_21[7], cty_val_se2_21[7], cty_val_se3_21[7], cty_val_se4_21[7]]
    
    c_se_20 = [cty_val_se1_20[0], cty_val_se2_20[0], cty_val_se3_20[0], cty_val_se4_20[0]]
    c_no_20 = [cty_val_se1_20[1], cty_val_se2_20[1], cty_val_se3_20[1], cty_val_se4_20[1]]
    c_dk_20 = [cty_val_se1_20[2], cty_val_se2_20[2], cty_val_se3_20[2], cty_val_se4_20[2]]
    c_fi_20 = [cty_val_se1_20[3], cty_val_se2_20[3], cty_val_se3_20[3], cty_val_se4_20[3]]
    c_de_20 = [cty_val_se1_20[4], cty_val_se2_20[4], cty_val_se3_20[4], cty_val_se4_20[4]]
    c_pl_20 = [cty_val_se1_20[5], cty_val_se2_20[5], cty_val_se3_20[5], cty_val_se4_20[5]]
    c_lt_20 = [cty_val_se1_20[6], cty_val_se2_20[6], cty_val_se3_20[6], cty_val_se4_20[6]]
    c_un_20 = [cty_val_se1_20[7], cty_val_se2_20[7], cty_val_se3_20[7], cty_val_se4_20[7]]
    
    c_se_19 = [cty_val_se1_19[0], cty_val_se2_19[0], cty_val_se3_19[0], cty_val_se4_19[0]]
    c_no_19 = [cty_val_se1_19[1], cty_val_se2_19[1], cty_val_se3_19[1], cty_val_se4_19[1]]
    c_dk_19 = [cty_val_se1_19[2], cty_val_se2_19[2], cty_val_se3_19[2], cty_val_se4_19[2]]
    c_fi_19 = [cty_val_se1_19[3], cty_val_se2_19[3], cty_val_se3_19[3], cty_val_se4_19[3]]
    c_de_19 = [cty_val_se1_19[4], cty_val_se2_19[4], cty_val_se3_19[4], cty_val_se4_19[4]]
    c_pl_19 = [cty_val_se1_19[5], cty_val_se2_19[5], cty_val_se3_19[5], cty_val_se4_19[5]]
    c_lt_19 = [cty_val_se1_19[6], cty_val_se2_19[6], cty_val_se3_19[6], cty_val_se4_19[6]]
    c_un_19 = [cty_val_se1_19[7], cty_val_se2_19[7], cty_val_se3_19[7], cty_val_se4_19[7]]
    
    c_se_18 = [cty_val_se1_18[0], cty_val_se2_18[0], cty_val_se3_18[0], cty_val_se4_18[0]]
    c_no_18 = [cty_val_se1_18[1], cty_val_se2_18[1], cty_val_se3_18[1], cty_val_se4_18[1]]
    c_dk_18 = [cty_val_se1_18[2], cty_val_se2_18[2], cty_val_se3_18[2], cty_val_se4_18[2]]
    c_fi_18 = [cty_val_se1_18[3], cty_val_se2_18[3], cty_val_se3_18[3], cty_val_se4_18[3]]
    c_de_18 = [cty_val_se1_18[4], cty_val_se2_18[4], cty_val_se3_18[4], cty_val_se4_18[4]]
    c_pl_18 = [cty_val_se1_18[5], cty_val_se2_18[5], cty_val_se3_18[5], cty_val_se4_18[5]]
    c_lt_18 = [cty_val_se1_18[6], cty_val_se2_18[6], cty_val_se3_18[6], cty_val_se4_18[6]]
    c_un_18 = [cty_val_se1_18[7], cty_val_se2_18[7], cty_val_se3_18[7], cty_val_se4_18[7]]
    
    
    c_ind = ['SE1', 'SE2', 'SE3', 'SE4']
    c_21 = pd.DataFrame({'SE':c_se_21, 'NO':c_no_21, 'DK':c_dk_21, 'FI':c_fi_21, 'DE':c_de_21, 'PL':c_pl_21, 'LT':c_lt_21, 'UNDEF.':c_un_21, 'Zone':c_ind})
    c_20 = pd.DataFrame({'SE':c_se_20, 'NO':c_no_20, 'DK':c_dk_20, 'FI':c_fi_20, 'DE':c_de_20, 'PL':c_pl_20, 'LT':c_lt_20, 'UNDEF.':c_un_20, 'Zone':c_ind})
    c_19 = pd.DataFrame({'SE':c_se_19, 'NO':c_no_19, 'DK':c_dk_19, 'FI':c_fi_19, 'DE':c_de_19, 'PL':c_pl_19, 'LT':c_lt_19, 'UNDEF.':c_un_19, 'Zone':c_ind})
    c_18 = pd.DataFrame({'SE':c_se_18, 'NO':c_no_18, 'DK':c_dk_18, 'FI':c_fi_18, 'DE':c_de_18, 'PL':c_pl_18, 'LT':c_lt_18, 'UNDEF.':c_un_18, 'Zone':c_ind})

    #MEF plots
    #fuels
    #2021
    
    f_coal_21 = [fuel_val_se1_21[0], fuel_val_se2_21[0], fuel_val_se3_21[0], fuel_val_se4_21[0]]
    f_lignite_21 = [fuel_val_se1_21[1], fuel_val_se2_21[1], fuel_val_se3_21[1], fuel_val_se4_21[1]]
    f_oil_21 = [fuel_val_se1_21[2], fuel_val_se2_21[2], fuel_val_se3_21[2], fuel_val_se4_21[2]]
    f_gas_cc_21 = [fuel_val_se1_21[3], fuel_val_se2_21[3], fuel_val_se3_21[3], fuel_val_se4_21[3]]
    f_gas_21 = [fuel_val_se1_21[4], fuel_val_se2_21[4], fuel_val_se3_21[4], fuel_val_se4_21[4]]
    f_bio_21 = [fuel_val_se1_21[5], fuel_val_se2_21[5], fuel_val_se3_21[5], fuel_val_se4_21[5]]
    f_nuc_21 = [fuel_val_se1_21[6], fuel_val_se2_21[6], fuel_val_se3_21[6], fuel_val_se4_21[6]]
    f_renewables_21 = [fuel_val_se1_21[7], fuel_val_se2_21[7], fuel_val_se3_21[7], fuel_val_se4_21[7]]
    
    f_coal_20 = [fuel_val_se1_20[0], fuel_val_se2_20[0], fuel_val_se3_20[0], fuel_val_se4_20[0]]
    f_lignite_20 = [fuel_val_se1_20[1], fuel_val_se2_20[1], fuel_val_se3_20[1], fuel_val_se4_20[1]]
    f_oil_20 = [fuel_val_se1_20[2], fuel_val_se2_20[2], fuel_val_se3_20[2], fuel_val_se4_20[2]]
    f_gas_cc_20 = [fuel_val_se1_20[3], fuel_val_se2_20[3], fuel_val_se3_20[3], fuel_val_se4_20[3]]
    f_gas_20 = [fuel_val_se1_20[4], fuel_val_se2_20[4], fuel_val_se3_20[4], fuel_val_se4_20[4]]
    f_bio_20 = [fuel_val_se1_20[5], fuel_val_se2_20[5], fuel_val_se3_20[5], fuel_val_se4_20[5]]
    f_nuc_20 = [fuel_val_se1_20[6], fuel_val_se2_20[6], fuel_val_se3_20[6], fuel_val_se4_20[6]]
    f_renewables_20 = [fuel_val_se1_20[7], fuel_val_se2_20[7], fuel_val_se3_20[7], fuel_val_se4_20[7]]
    
    f_coal_19 = [fuel_val_se1_19[0], fuel_val_se2_19[0], fuel_val_se3_19[0], fuel_val_se4_19[0]]
    f_lignite_19 = [fuel_val_se1_19[1], fuel_val_se2_19[1], fuel_val_se3_19[1], fuel_val_se4_19[1]]
    f_oil_19 = [fuel_val_se1_19[2], fuel_val_se2_19[2], fuel_val_se3_19[2], fuel_val_se4_19[2]]
    f_gas_cc_19 = [fuel_val_se1_19[3], fuel_val_se2_19[3], fuel_val_se3_19[3], fuel_val_se4_19[3]]
    f_gas_19 = [fuel_val_se1_19[4], fuel_val_se2_19[4], fuel_val_se3_19[4], fuel_val_se4_19[4]]
    f_bio_19 = [fuel_val_se1_19[5], fuel_val_se2_19[5], fuel_val_se3_19[5], fuel_val_se4_19[5]]
    f_nuc_19 = [fuel_val_se1_19[6], fuel_val_se2_19[6], fuel_val_se3_19[6], fuel_val_se4_19[6]]
    f_renewables_19 = [fuel_val_se1_19[7], fuel_val_se2_19[7], fuel_val_se3_19[7], fuel_val_se4_19[7]]
    
    f_coal_18 = [fuel_val_se1_18[0], fuel_val_se2_18[0], fuel_val_se3_18[0], fuel_val_se4_18[0]]
    f_lignite_18 = [fuel_val_se1_18[1], fuel_val_se2_18[1], fuel_val_se3_18[1], fuel_val_se4_18[1]]
    f_oil_18 = [fuel_val_se1_18[2], fuel_val_se2_18[2], fuel_val_se3_18[2], fuel_val_se4_18[2]]
    f_gas_cc_18 = [fuel_val_se1_18[3], fuel_val_se2_18[3], fuel_val_se3_18[3], fuel_val_se4_18[3]]
    f_gas_18 = [fuel_val_se1_18[4], fuel_val_se2_18[4], fuel_val_se3_18[4], fuel_val_se4_18[4]]
    f_bio_18 = [fuel_val_se1_18[5], fuel_val_se2_18[5], fuel_val_se3_18[5], fuel_val_se4_18[5]]
    f_nuc_18 = [fuel_val_se1_18[6], fuel_val_se2_18[6], fuel_val_se3_18[6], fuel_val_se4_18[6]]
    f_renewables_18 = [fuel_val_se1_18[7], fuel_val_se2_18[7], fuel_val_se3_18[7], fuel_val_se4_18[7]]
    
    
    f_21 = pd.DataFrame({'Coal':f_coal_21, 'Lignite':f_lignite_21, 'Oil':f_oil_21, 'Gas CC':f_gas_cc_21, 'Gas':f_gas_21, 'Biomass':f_bio_21, 'Nuclear':f_nuc_21, 'Renewables':f_renewables_21, 'Zone':c_ind})
    f_20 = pd.DataFrame({'Coal':f_coal_20, 'Lignite':f_lignite_20, 'Oil':f_oil_20, 'Gas CC':f_gas_cc_20, 'Gas':f_gas_20, 'Biomass':f_bio_20, 'Nuclear':f_nuc_20, 'Renewables':f_renewables_20, 'Zone':c_ind})
    f_19 = pd.DataFrame({'Coal':f_coal_19, 'Lignite':f_lignite_19, 'Oil':f_oil_19, 'Gas CC':f_gas_cc_19, 'Gas':f_gas_19, 'Biomass':f_bio_19, 'Nuclear':f_nuc_19, 'Renewables':f_renewables_19, 'Zone':c_ind})
    f_18 = pd.DataFrame({'Coal':f_coal_18, 'Lignite':f_lignite_18, 'Oil':f_oil_18, 'Gas CC':f_gas_cc_18, 'Gas':f_gas_18, 'Biomass':f_bio_18, 'Nuclear':f_nuc_18, 'Renewables':f_renewables_18, 'Zone':c_ind})

    
    c_21.index = c_21['Zone']
    c_20.index = c_20['Zone']
    c_19.index = c_19['Zone']
    c_18.index = c_18['Zone']
    f_21.index = f_21['Zone']
    f_20.index = f_20['Zone']
    f_19.index = f_19['Zone']
    f_18.index = f_18['Zone']
    
    c_21 = c_21.drop('Zone', axis=1)
    c_20 = c_20.drop('Zone', axis=1)
    c_19 = c_19.drop('Zone', axis=1)
    c_18 = c_18.drop('Zone', axis=1)
    f_21 = f_21.drop('Zone', axis=1)
    f_20 = f_20.drop('Zone', axis=1)
    f_19 = f_19.drop('Zone', axis=1)
    f_18 = f_18.drop('Zone', axis=1)
    
    #matplotlib
    #plt.style.use("seaborn")
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    #data handling
    #df = pd.DataFrame({'SE':, 'NO':, 'DK':, 'FI':, 'DE':, 'PL':, 'LT':, 'UNDEF.':})
    #plt.subplot(1,4,1)
    #c_21 = c_21.set_index('Zone')
    fig, axes = plt.subplots(nrows=2, ncols=4)
    #colors = plt.cm.Paired(np.linspace(0, 1, 10))
    colors = ['cornflowerblue', 'steelblue', 'lightblue', 'lightsteelblue', 'lightyellow', 'bisque', 'lightcoral', 'palegreen']
    ax1 = c_18.iloc[0:32, 0:8].plot.barh(ax=axes[0,0], align='center', stacked=True, figsize=(14, 6), color=colors, legend=False, xticks=[0,8760/4, 8760/2, 3*8760/4, 8760])#['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']) #fuel colors: color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']
    ax2 = c_19.iloc[0:32, 0:8].plot.barh(ax=axes[0,1], align='center', stacked=True, figsize=(14, 6), color=colors, legend=False, xticks=[0,8760/4, 8760/2, 3*8760/4, 8760])#['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']) #fuel colors: color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']
    ax3 = c_20.iloc[0:32, 0:8].plot.barh(ax=axes[0,2], align='center', stacked=True, figsize=(14, 6), color=colors, legend=False, xticks=[0,8760/4, 8760/2, 3*8760/4, 8760])#['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']) #fuel colors: color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']
    ax4 = c_21.iloc[0:32, 0:8].plot.barh(ax=axes[0,3], align='center', stacked=True, figsize=(14, 6), color=colors, legend=False, xticks=[0,8760/4, 8760/2, 3*8760/4, 8760])#['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']) #fuel colors: color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']
    ax5 = f_18.iloc[0:24, 0:8].plot.barh(ax=axes[1,0], align='center', stacked=True, figsize=(14, 6), legend=False, xticks=[0,8760/4, 8760/2, 3*8760/4, 8760], color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'darkgreen', 'orchid', 'lightseagreen']) #fuel colors: color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']
    ax6 = f_19.iloc[0:24, 0:8].plot.barh(ax=axes[1,1], align='center', stacked=True, figsize=(14, 6), legend=False, xticks=[0,8760/4, 8760/2, 3*8760/4, 8760], color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'darkgreen', 'orchid', 'lightseagreen']) #fuel colors: color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']
    ax7 = f_20.iloc[0:24, 0:8].plot.barh(ax=axes[1,2], align='center', stacked=True, figsize=(14, 6), legend=False, xticks=[0,8760/4, 8760/2, 3*8760/4, 8760], color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'darkgreen', 'orchid', 'lightseagreen']) #fuel colors: color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']
    ax8 = f_21.iloc[0:24, 0:8].plot.barh(ax=axes[1,3], align='center', stacked=True, figsize=(14, 6), legend=False, xticks=[0,8760/4, 8760/2, 3*8760/4, 8760], color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'darkgreen', 'orchid', 'lightseagreen']) #fuel colors: color=['dimgray', 'maroon', 'rebeccapurple', 'peru', 'gold', 'lightseagreen']
    plt.tight_layout()
    plt.margins(y=0.3, tight=True)
    #title = plt.title('2020', pad=60, fontsize=40)
    #title.set_position([.5, 1.02])
    ax1.set_title('2018', fontsize=15)
    ax2.set_title('2019', fontsize=15)
    ax3.set_title('2020', fontsize=15)
    ax4.set_title('2021', fontsize=15)
    ax1.set_ylabel('')
    ax5.set_ylabel('')
    ax1.set_xlim([0,8760])
    ax2.set_xlim([0,8760])
    ax3.set_xlim([0,8760])
    ax4.set_xlim([0,8760])
    ax5.set_xlim([0,8760])
    ax6.set_xlim([0,8760])
    ax7.set_xlim([0,8760])
    ax8.set_xlim([0,8760])
    ax2.get_yaxis().set_visible(False)
    ax3.get_yaxis().set_visible(False)
    ax4.get_yaxis().set_visible(False)
    ax6.get_yaxis().set_visible(False)
    ax7.get_yaxis().set_visible(False)
    ax8.get_yaxis().set_visible(False)
    fig.tight_layout()
    ax1.tick_params(axis='y', which='major', labelsize=15)
    ax5.tick_params(axis='y', which='major', labelsize=15)
    handles, labels = ax4.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.212, -0.025, 0.6, 0.52), mode='expand', ncol=18, borderaxespad=-1, prop={'size': 15,})
    handles, labels = ax8.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.11, -0.485, 0.8, 0.52), mode='expand', ncol=8, borderaxespad=-1, prop={'size': 15,})
    # for label in (ax1.get_xticklabels() + ax1.get_yticklabels()):
    #     label.set_fontsize(30)
    # legend = fig.legend(loc='center',
    #    frameon=False,
    #    bbox_to_anchor=(0., 1.02, 1., .102), 
    #    mode='expand', 
    #    ncol=8, 
    #    borderaxespad=-.46,
    #    prop={'size': 25, 'family':'Calibri'})
    # for p in ax1.patches:
    #     width, height = p.get_width(), p.get_height()
    #     x, y = p.get_xy() 
    #     ax1.text(x+width/2, 
    #             y+height/2, 
    #             '{:.0f}'.format(width), 
    #             horizontalalignment='center', 
    #             verticalalignment='center',
    #             color='black',
    #             fontsize=14)
    ax1.axes.xaxis.set_ticklabels([])
    ax2.axes.xaxis.set_ticklabels([])
    ax3.axes.xaxis.set_ticklabels([])
    ax4.axes.xaxis.set_ticklabels([])
    ax5.axes.xaxis.set_ticklabels([])
    ax6.axes.xaxis.set_ticklabels([])
    ax7.axes.xaxis.set_ticklabels([])
    ax8.axes.xaxis.set_ticklabels([])
    plt.show()



elif what == "countries":
    XEFs_21 = elmada.linus_part.get_emissions_trade(year=2021, country="SE3", all_countries="yes", ef_type="XEFs", cache=False)
    XEFs_20 = elmada.linus_part.get_emissions_trade(year=2020, country="SE3", all_countries="yes", ef_type="XEFs", cache=False)
    XEFs_19 = elmada.linus_part.get_emissions_trade(year=2019, country="SE3", all_countries="yes", ef_type="XEFs", cache=False)
    XEFs_18 = elmada.linus_part.get_emissions_trade(year=2018, country="SE3", all_countries="yes", ef_type="XEFs", cache=False)

    SE1_area = []
    SE2_area = []
    SE3_area = []
    SE4_area = []
    DK_area = []
    NO_area = []
    FI_area = []
    DE_area = []
    PL_area = []
    LT_area = []
    for i in range(8760*4+24):
        SE1_area.append("SE1")
        SE2_area.append("SE2")
        SE3_area.append("SE3")
        SE4_area.append("SE4")
        DK_area.append("DK")
        NO_area.append("NO")
        FI_area.append("FI")
        DE_area.append("DE")
        PL_area.append("PL")
        LT_area.append("LT")

    area_lst = SE1_area
    area_lst.extend(SE2_area)
    area_lst.extend(SE3_area)
    area_lst.extend(SE4_area)
    area_lst.extend(NO_area)
    area_lst.extend(DK_area)
    area_lst.extend(FI_area)
    area_lst.extend(DE_area)
    area_lst.extend(PL_area)
    area_lst.extend(LT_area)

    all_xefs = []
    all_xefs.extend(XEFs_18.iloc[:,0])
    all_xefs.extend(XEFs_19.iloc[:,0])
    all_xefs.extend(XEFs_20.iloc[:,0])
    all_xefs.extend(XEFs_21.iloc[:,0])
    all_xefs.extend(XEFs_18.iloc[:,7])
    all_xefs.extend(XEFs_19.iloc[:,7])
    all_xefs.extend(XEFs_20.iloc[:,7])
    all_xefs.extend(XEFs_21.iloc[:,7])
    all_xefs.extend(XEFs_18.iloc[:,8])
    all_xefs.extend(XEFs_19.iloc[:,8])
    all_xefs.extend(XEFs_20.iloc[:,8])
    all_xefs.extend(XEFs_21.iloc[:,8])
    all_xefs.extend(XEFs_18.iloc[:,9])
    all_xefs.extend(XEFs_19.iloc[:,9])
    all_xefs.extend(XEFs_20.iloc[:,9])
    all_xefs.extend(XEFs_21.iloc[:,9])
    all_xefs.extend(XEFs_18.iloc[:,1])
    all_xefs.extend(XEFs_19.iloc[:,1])
    all_xefs.extend(XEFs_20.iloc[:,1])
    all_xefs.extend(XEFs_21.iloc[:,1])
    all_xefs.extend(XEFs_18.iloc[:,2])
    all_xefs.extend(XEFs_19.iloc[:,2])
    all_xefs.extend(XEFs_20.iloc[:,2])
    all_xefs.extend(XEFs_21.iloc[:,2])
    all_xefs.extend(XEFs_18.iloc[:,3])
    all_xefs.extend(XEFs_19.iloc[:,3])
    all_xefs.extend(XEFs_20.iloc[:,3])
    all_xefs.extend(XEFs_21.iloc[:,3])
    all_xefs.extend(XEFs_18.iloc[:,4])
    all_xefs.extend(XEFs_19.iloc[:,4])
    all_xefs.extend(XEFs_20.iloc[:,4])
    all_xefs.extend(XEFs_21.iloc[:,4])
    all_xefs.extend(XEFs_18.iloc[:,5])
    all_xefs.extend(XEFs_19.iloc[:,5])
    all_xefs.extend(XEFs_20.iloc[:,5])
    all_xefs.extend(XEFs_21.iloc[:,5])
    all_xefs.extend(XEFs_18.iloc[:,6])
    all_xefs.extend(XEFs_19.iloc[:,6])
    all_xefs.extend(XEFs_20.iloc[:,6])
    all_xefs.extend(XEFs_21.iloc[:,6])
    # all_xefs.extend(XEFs.iloc[:,7])
    # all_xefs.extend(XEFs.iloc[:,8])
    # all_xefs.extend(XEFs.iloc[:,9])
    # all_xefs.extend(XEFs.iloc[:,1])
    # all_xefs.extend(XEFs.iloc[:,2])
    # all_xefs.extend(XEFs.iloc[:,3])
    # all_xefs.extend(XEFs.iloc[:,4])
    # all_xefs.extend(XEFs.iloc[:,5])
    # all_xefs.extend(XEFs.iloc[:,6])

    xefs = pd.DataFrame({'XEFs':all_xefs,
                        'Area':area_lst
                        })
    

    mainfont = {'fontname':'Arial'}
    #plotting
    plt.style.use("seaborn-whitegrid") #seaborn-whitegrid
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    f, (ax1) = plt.subplots()
    #ax1.set_yticks(['SE1', 'SE2', 'SE3'],fontsize=6)#, **font
    #ax2.set_yticks(['SE4'],fontsize=6)#, **font
    pal = sns.color_palette("crest",10) #Pastel1
    #Total
    all_xefs = sns.violinplot(data=xefs, x="Area", y="XEFs", scale='width', cut=0, palette=pal, lw=1)
    #xef_total = sns.violinplot(ax=ax1, cut=0, x="MEFs", y="Area", data=efs_total, bw=0.2, width=0.9, palette=pal, legend=False, order=['SE1','SE2','SE3', 'SE4'], linewidth=0.3, inner=None, zorder=1)
    ax1.set_ylabel("AEF [gCO$_2$eq/kWh]", fontsize=35, **mainfont)
    ax1.set_xlabel("", fontsize=30, **mainfont)
    ax1.set_ylim(0,1000)
    ax1.tick_params(axis='both', which='major', labelsize=30)
    ax1.tick_params(axis='both', which='minor', labelsize=30)
    #plt.legend(title="Zone", bbox_to_anchor=(1.13,1.05), prop={'size': 20,})
    ax1.grid(linewidth=0.6)
    ax1.grid(axis='x')
    for axis in ['top','bottom','left','right']:
        ax1.spines[axis].set_linewidth(0.6)
    #plt.title('MEF [g$_{CO_2eq}$/kWh]', fontsize=8, x=-0.1, y=0.5, **mainfont)
    plt.show()


