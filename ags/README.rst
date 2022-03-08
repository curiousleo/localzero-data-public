AGS Master and KE list
=======================

The KE list includes all active, currently inactive and befriended teams according to https://mitmachen-wiki.germanzero.org/wiki/index.php?title=Klimaentscheide:Klimaentscheid-Teams 

This Master list contains only AGS, where no change to the AGS (such as integration of another AGS) happened since the beginning of 2018.  It does not contain AGS that had events happen to it since 2018 because those the generator cannot deal with anyway.

The AGS list includes AGS for states, districts and cities in Germany including the one for Germany itself.

Generated this way:

.. code-block:: console

   { echo 'ags,description' ; curl https://www.xrepository.de/api/xrepository/urn:xoev-de:bund:destatis:bevoelkerungsstatistik:codeliste:ags.historie_2021-12-31/download/Destatis.AGS.Historie_2021-12-31.json | jq -r '[ .daten[] | select(.[4] == null) | [ .[1], .[2], .[3] | sub("(?<d>[0-9]{2})\\.(?<m>[0-9]{2})\\.(?<y>[0-9]{4})"; "\(.y)-\(.m)-\(.d)")] ] | sort_by(.[2]) | .[] | @csv' | fgrep -B 99999 ',"2018-01-01"' | sed -r 's/,"[^"]+"$//' } > master.csv


Changes German Zero: 
--------------------

11.02.2022
~~~~~~~~~~

- Removed "02000000","Hamburg, Freie und Hansestadt" as "02000000","Hamburg" was already in the list
- Removed all sub ags in Hamburg, Bremen and Berlin ("02XXXXXX" , "04XXXXXX" and "11XXXXXX") except "02000000" , "04000000" and "11000000" 
   as we dont have any data on them in most of our data tables
- Removed weird AGS "07000999","Gemeinsames deutsch-luxemburgisches Hoheitsgebiet"
- Removed weird AGS "03901999","Nds-Küstengewässer(Gemarkung Nordsee)"
- Removed weird AGS "13000999","Küstengewässer einschl. Anteil am Festlandsockel"
- updated "13058119","Wedendorfersee" to correct AGS "13074092","Wedendorfersee"

- Removed Landkreis "03156000","Osterode am Harz" as it was incorperated into Landkreis Göttingen "03159000" in 2016

17.02.2022
~~~~~~~~~~

- Include Greifswald "13075039" in master.csv. There was a change in 2021: the name was updated, the AGS was unaffected

