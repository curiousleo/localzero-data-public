AGS Master list
===============

Generated this way:

.. code-block:: console

    $ { echo 'ags,description' ; curl https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:ags_2018-08-31/download/AGS_2018-08-31.json | jq -r '.daten[] | @csv' } > ags.csv
