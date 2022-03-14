Area kinds
==========
Area kinds provide a method to categorize communities by type (and then deal with them differently in the LocalZero calculation).
The Area kinds-table is only used in the transport sector. There are different categorization keys.
A more detailed explanation of the RegioStar can be found under https://www.bmvi.de/SharedDocs/DE/Anlage/G/regiostar-raumtypologie.pdf?__blob=publicationFile
We use the RegioStar7 (rt7 in the .csv) by the 
bmvi (Bundesministerium für Verkehr und digitale Infrastruktur) that categorizes into:

- **71**: Metropole - Stadtregion
- **72**: Regiopolen und Großstädte - Stadtregion
- **73**: Mittelstädte, städtischer Raum - Stadtregion
- **74**: Kleinstädtischer, dörflicher Raum - Stadtregion
- **75**: Zentrale Städte - ländliche Region
- **76**: Mittelstädte, städtischer Raum - ländliche Region
- **77**: Kleinstädtischer, dörflicher Raum - ländliche Region

The RegioStar7 is used in the transport 2018 calculation script and can be found under https://www.bmvi.de/SharedDocs/DE/Artikel/G/regionalstatistische-raumtypologie.html.

The Area kind categorization key also originates in the RegioStar7 key and categorizes into 3 categories:

- city (Stadt)        71,72
- smcty (Halbstadt)   73,75
- rural (Land)        74,76,77

This key is used in the transport 203X sector. The translation is taken from the "Klimaneutrales Deutschland" Study by agora-energiewende (Page 87, Table 3):
https://www.agora-energiewende.de/veroeffentlichungen/klimaneutrales-deutschland/



