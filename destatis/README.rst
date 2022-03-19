Destatis Traffic Data
=====================

Source: Destatis  "Verkehr:  Personenverkehr mit Bussen und Bahnen" (2018) - 1.10   
Fahrleistungen im Schienen- und Liniennahverkehr nach Art des Verkehrsmittels und Kreisen  S. 27-31


https://www.destatis.de/DE/Themen/Branchen-Unternehmen/Transport-Verkehr/Personenverkehr/Publikationen/Downloads-Personenverkehr/personenverkehr-busse-bahnen-vierteljahr-2080310183234.pdf?__blob=publicationFile&v=3

Comment Anne Schwob:
Hinweise zur Statistik: 
Die Daten werden jährlich bei allen Großunternehmen mit mindestens 250 000 Fahrgästen und bei
Stichprobenunternehmen mit weniger als 250 000 Fahrgästen erhoben. Die Angaben im Linienennahverkehr
zur Fahrleistung beziehen sich auf den Kreis der tatsächlichen Leistungserbringung (NUTS 3-Ebene).

Data:
- total_mega_km -> Insgesamt [Mio. Fahrzeug-km]
- rail_mega_km -> Eisenbahn [Mio. Fz-km]
- metro_mega_km -> SSU-Bahn [Mio. Fz-km]
- bus_mega_km -> Omnibus [Mio. Fz-km]



Changes GermanZero:
-------------------

transferred Data from old "Aachen, Kreis" (05354000) to "Düren, Kreis" (05358000), because
we assumed a data error as the ags key 05334000 occured twice. 

.. code-block::

    from:
    05334000,20.2,1.4,0.0,18.7  <- "Städteregion Aachen (einschl. Stadt Aachen)"
    05354000,8.8,1.1,0.0,7.8    <- "Aachen, Kreis"
    05358000,,,,                <- "Düren, Kreis"

    to: 
    05334000,20.2,1.4,0.0,18.7  <- "Städteregion Aachen (einschl. Stadt Aachen)"
    05358000,8.8,1.1,0.0,7.8    <- "Düren, Kreis"
