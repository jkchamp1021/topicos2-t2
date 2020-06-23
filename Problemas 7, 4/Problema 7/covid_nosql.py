
import time
import psycopg2
mydb = psycopg2.connect(
  host="localhost",
  user="topicos2user",
  password="12345",
  database="topicos2"
)
mycursor = mydb.cursor()
tiempo = time.time()
mycursor.execute("SELECT SUM((data->>'casos')::integer) as casos, data->>'distrito' as distrito FROM public.covid group by data->>'distrito' order by casos desc LIMIT 3;")
res =  mycursor.fetchall()
tiempo = time.time() - tiempo
print(tiempo)
for x in res:
  print(x)

tiempo = time.time()
mycursor.execute("SELECT data->'id' as id,data->'provincia' as provincia, data->'distrito' as distrito, data->'nombre' as corregimiento, data->'sede' as sede, data->'casos' as casos  FROM public.covid where data->'id' = '8';")
res =  mycursor.fetchall()
tiempo = time.time() - tiempo
print(tiempo)
for x in res:
  print(x)


tiempo = time.time()
mycursor.execute("SELECT avg((data->'casos')::integer) as promedio FROM public.covid where data->'id' = '11' or data->'id' = '12' or data->'id' = '13';")
res =  mycursor.fetchall()
tiempo = time.time() - tiempo
print(tiempo)
for x in res:
  print(x)


tiempo = time.time()
mycursor.execute("WITH pC AS( SELECT avg((data->'casos')::integer) as prom FROM public.covid where data->'id' = '2' and data->'distrito' != '\"Boquete\"'), pB AS( SELECT avg((data->'casos')::integer) as prom FROM public.covid where data->'id' = '2' and data->'distrito' = '\"Boquete\"') SELECT ((pC.prom-pB.prom)/pB.prom)*100 as desviacion from pC,pB;")
res =  mycursor.fetchall()
tiempo = time.time() - tiempo
print(tiempo)
for x in res:
  print(x)


  