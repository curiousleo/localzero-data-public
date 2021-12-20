# Arbeitsleitfaden

## Struktur
Die `kommunentabelle.csv` gibt Kerninformationen zu Kommunen vor.
Für jedes Attribut (z.B. "Emissionen Verkehr") existiert eine Datentabelle im Ordner `attribute` nach folgendem Schema:
|AGS der Kommune|2015|2016|2018|2019|2020|...|
|-|-|-|-|-|-|-|
||||||||

Im Ordner `source` liegen die originalen Datentabellen der genutzten Datenquellen.
Zu diesen befindet sich im Ordner `license` jeweils die zugehörige Lizenzvereinbarung.

## Datenversionierung

### Benennung von Commit-Messages

Jede Commit-Message muss nach folgendem Schema gestaltet werden:

*TODO*

Ziel ist es bei jedem veränderten Datenpunkt nachverfolgen zu können aus welcher Quelle diese Information stammt um ggf. sich als ungenau herausstellende Quellen entfernen zu können und Datenherkunft nachverfolgbar zu machen.

### Pull-Request Kontrollen und Workflow
