# elmada-with-trading
Dynamic grid emission factors for northern Europe considering inter-country electricity trading. Based on elmada by @mfleschutz (https://github.com/DrafProject/elmada).
Used and explained in "Grid-supported electrolytic hydrogen production: Cost and climate impact using dynamic emission factors" by Engstam, L., Janke, L., Sundberg, C., Nordberg, Å. (2023) in Energy Conversion and Management, Volume 293, 117458. DOI: https://doi.org/10.1016/j.enconman.2023.117458

Installation:
- Install original elmada as per https://github.com/DrafProject/elmada
- Copy the contents of the elmada-with-trading folder to the original elmada folder and replace all existing files

Use:
- Run simulation by importing elmada.trading and exectuing the following command: elmada.trading.get_emissions_trade().
  The following input variables can be defined: \
  _year_ - year of simulation. 2018 - 2021 is available \
  _country_ - country/bidding zone. All countries included in original elmada are possible, but trading data only included for SE(1/2/3/4), NO, FI, DK, DE, PL, LT and transmission data only for SE(1/2/3/4) \
  _ef_type_ - average grid-mix ("AEFs") or marginal emission factors ("MEFs") or both ("both") \
  **Non-obligatory inputs** \
  _all_countries_ - "yes"/"no". Return data for all countries included in article analysis (SE(1/2/3/4), NO, FI, DK, DE, PL, LT) \
  _import_fraction_ - "yes"/"no". Return the annual fraction of imported (non-Swedish) electricity consumed in all four Swedish bidding zones. \
- Example: elmada.trading.get_emissions_trade(year=2021, country="SE3", ef_type="AEFs") returns average grid-mix emission factors for SE3 in 2021.

Pre-calculated emission factor data for SE(1/2/3/4) in 2018 - 2021 can be found at https://github.com/lengstam/emission-factors/
