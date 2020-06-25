#Jhoan de León
#Ricky Chan
#Deepak Wadhwani

import sqlite3
import copy

ConnectionDB = sqlite3.connect('babynames.sql')
Connection = ConnectionDB.cursor()

Connection.execute('''CREATE TABLE IF NOT EXISTS nombres
              (id integer NOT NULL PRIMARY KEY, rank text, name text, sex text, births real)''')


with open("names2018.txt") as f:
    file = f.readlines()
    orig = [line.split() for line in file]
    male = copy.deepcopy(orig)
    female = copy.deepcopy(orig)
    Cont=1
    for lineM in male[1:]:
        del lineM[-1]
        lineM.append("M")
        lineM.append(Cont)
        Cont+=1
    for lineF in female[1:]:
        del lineF[-2]
        lineF.append("F")
        lineF.append(Cont)
        Cont+=1
    with open("births2018.txt") as f2:
        file = f2.readlines()
        births = [line.split() for line in file]
        birthsM = [item[2] for item in births[3:]]
        birthsF = [item[4] for item in births[3:]]
        ctrl=0
        for line in male[1:]:
            if(ctrl<20):
                line.append(birthsM[ctrl])
            else:
                line.append(None)
            ctrl+=1
        ctrl=0
        for line in female[1:]:
            if(ctrl<20):
                line.append(birthsF[ctrl])
            else:
                line.append(None)
            ctrl+=1
    male.pop(0)
    female.pop(0)
    
Connection.executemany('''INSERT INTO nombres(rank,name,sex,id,births) VALUES (?, ?, ?, ?, ?) on conflict do nothing''',male)
Connection.executemany('''INSERT INTO nombres(rank,name,sex,id,births) VALUES (?, ?, ?, ?, ?) on conflict do nothing''',female)

result=Connection.execute('''SELECT name FROM nombres where sex = 'M' LIMIT 100 ''')
print("100 primeros nombres masculinos: ")
for row in result:
    print (row)

print("\n\n100 primeros nombres femeninos: ")
result=Connection.execute('''SELECT name FROM nombres where sex = 'F' LIMIT 100 ''')
for row in result:
    print (row)

print("\n\nNombres con 4 letras o menos: ")
result=Connection.execute('''SELECT rank, name FROM nombres where
    name LIKE ''
  OR name LIKE '_' 
  OR name LIKE '__'
  OR name LIKE '___'
  OR name LIKE '____' ''')
for row in result:
    print (row)

print("\n\nNombres femeninos con las letras w,x,y,z: ")
result=Connection.execute('''SELECT name FROM nombres where sex = 'F' AND (name like '%w%' or name like '%x%' or name like '%y%' or name like '%z%') ''')
for row in result:
    print (row)

print("\n\nNombres con dos letras repetidas aa, cc, pp: ")
result=Connection.execute('''SELECT name FROM nombres where name like '%aa%' or name like '%cc%' or name like '%pp%' ''')
for row in result: 
    print(row)