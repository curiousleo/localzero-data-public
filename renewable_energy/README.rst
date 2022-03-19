Renewable Energy Data
=====================

This data originates in the "Marktstammdatenregister" (https://www.marktstammdatenregister.de/MaStR/Einheit/Einheiten/OeffentlicheEinheitenuebersicht). This list
contains all registered and installed renewable energy producers (single solar cells, wind turbines etc.) and provides information on the current status, the units
power, the date of installation etc. It also provides the location or more precisely the name of the city/village/town and the "Postleitzahl", where the unit is located.
This allows us to sum over all units within one commune and calculate the locally installed renewable power grouped by 

- pv (power of local photo voltaic cells)
- wind_on (power of local onshore wind turbines)
- biomass (power of local biomas power plants)
- geothermal (power of local geothermal sources)
- water (power of local water power plants)

This summation and bucketing to all ags keys was done in excel and needs to be repeated in python soon as the we choose an ags ist for 2021 instead of 2018 
(We will provide a script as soon as this is done.).
Therefore all ags keys from 2018 that had changes after 2018 are not part of the list right now. Only their ags successors are conatined at the moment.
