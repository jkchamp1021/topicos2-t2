import mysql.connector  #MySQL como motor para la base de datos SQL
import time
import psycopg2
mydb = mysql.connector.connect(
  host="localhost",
  user="topicos2user",
  password="12345",
  database="topicos2"
)
mycursor = mydb.cursor()
tiempo = time.time()
mycursor.execute("SELECT distritos.nombre, sum(casos) as 'casos' FROM topicos2.distritos inner join corregimientos on corregimientos.distrito = distritos.iddistritos group by nombre order by casos desc limit 3;")
res =  mycursor.fetchall()
tiempo = time.time() - tiempo
print(tiempo)
for x in res:
  print(x)

tiempo = time.time()
mycursor.execute("SELECT * FROM topicos2.provincia inner join distritos on distritos.provincia = provincia.idprovincia inner join corregimientos on corregimientos.distrito = distritos.iddistritos where idprovincia = 8;")
res =  mycursor.fetchall()
tiempo = time.time() - tiempo
print(tiempo)
for x in res:
  print(x)


tiempo = time.time()
mycursor.execute("SELECT AVG(casos) FROM topicos2.provincia inner join distritos on distritos.provincia = provincia.idprovincia inner join corregimientos on corregimientos.distrito = distritos.iddistritos where idprovincia = 11 or idprovincia = 12 or idprovincia = 13;")
res =  mycursor.fetchall()
tiempo = time.time() - tiempo
print(tiempo)
for x in res:
  print(x)


tiempo = time.time()
mycursor.execute("SELECT @pc := AVG(casos), 'Porcentaje de Chiriquí' as 'Dato' FROM topicos2.provincia inner join distritos on distritos.provincia = idprovincia inner join corregimientos on corregimientos.distrito = iddistritos where idprovincia = 2 and iddistritos != 8 union all SELECT concat(((@pc - AVG(casos))/AVG(casos))*100, '%'), 'Desviación' FROM topicos2.corregimientos where distrito = 8;")
res =  mycursor.fetchall()
tiempo = time.time() - tiempo
print(tiempo)
for x in res:
  print(x)


  