AGS Master list
===============

This list contains only AGS, where no change to the AGS (such as integration of another AGS) has happened since the 
end of 2006, which is when destatis started to maintain the data.  We could certainly bump this up to our reference
year quite easily (2018).  This was just a very quick first hack before the silent go-live.

After the silent go-live we should eventually figure out how to deal with AGS that had events since the reference
year.

Generated this way:

.. code-block:: console

   { echo 'ags,description' ; curl https://www.xrepository.de/api/xrepository/urn:xoev-de:bund:destatis:bevoelkerungsstatistik:codeliste:ags.historie_2021-12-31/download/Destatis.AGS.Historie_2021-12-31.json | jq -r '.daten[] | select(.[4] == null and .[3] == "31.12.2006") | [ .[1], .[2] ] | @csv ' }  > master.csv
