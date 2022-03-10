import csv
import os

#Input------------
table1name = "master"
table2name = "masterOld"

table1Path = "ags/master.csv"
table2Path = "ags/masterOLD.csv"


#-------------
table1List = []
table2List = []

table1dict = {}
table2dict = {}


with open(table1Path) as table1:
    table1R = csv.reader(table1,delimiter=',')
    _ = next(table1R)
    for row in table1R:
        if "".join([row[n] for n in range(1,len(row))]) == "":
            continue
        table1List.append(row[0])
        table1dict[row[0]] = " ".join([row[n] for n in range(1,len(row))])
        
with open(table2Path) as table2:
    table2R = csv.reader(table2,delimiter=',')
    _= next(table2R)
    for row in table2R:
        if "".join([row[n] for n in range(1,len(row))]) == "":
            continue

        table2List.append(row[0])
        table2dict[row[0]] = " ".join([row[n] for n in range(1,len(row))])

onlyin1 = []
for key in table1List:
    if key not in table2List:
        onlyin1.append(key)

onlyin2 = []
for key in table2List:
    if key not in table1List:
        onlyin2.append(key)

for key in onlyin2:
    print(key + " ",table2dict[key])

if not os.path.exists("diffs/diff"+table1name+table2name):
    os.makedirs("diffs/diff"+table1name+table2name)

with open("diffs/diff"+table1name+table2name+"/onlyIn"+table1name+".txt","w",newline="") as table1W:
    for key in onlyin1:
        table1W.write(key + " "+table1dict[key]+"\n")

with open("diffs/diff"+table1name+table2name+"/onlyIn"+table2name+".txt","w",newline="") as table2W:
    for key in onlyin2:
        table2W.write(key + " "+table2dict[key]+"\n")


print(table1name + " length "+ str(len(onlyin1)))
print(table2name + " length "+ str(len(onlyin2)))         

