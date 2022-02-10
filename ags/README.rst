AGS Master list
===============

This list contains only AGS, where no change to the AGS (such as integration of another AGS) happened since the beginning of 2018.  It does not contain AGS that had events happen to it since 2018 because those the generator cannot deal with anyway.

The AGS list includes AGS for states, districts and cities in Germany including the one for Germany itself.

Generated this way:

.. code-block:: console

   { echo 'ags,description' ; curl https://www.xrepository.de/api/xrepository/urn:xoev-de:bund:destatis:bevoelkerungsstatistik:codeliste:ags.historie_2021-12-31/download/Destatis.AGS.Historie_2021-12-31.json | jq -r '[ .daten[] | select(.[4] == null) | [ .[1], .[2], .[3] | sub("(?<d>[0-9]{2})\\.(?<m>[0-9]{2})\\.(?<y>[0-9]{4})"; "\(.y)-\(.m)-\(.d)")] ] | sort_by(.[2]) | .[] | @csv' | fgrep -B 99999 ',"2018-01-01"' | sed -r 's/,"[^"]+"$//' } > master.csv
