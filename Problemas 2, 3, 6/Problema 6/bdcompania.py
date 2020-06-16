import sqlite3
import os.path

## ASEGURARSE DE BORRAR EL ARCHIVO company.sql EN CASO DE VOLVER A CORRER EL CODIGO NUEVAMENTE ##

mirutaInformacion = os.path.abspath(os.path.dirname(__file__))
rutaInformacion = os.path.join(mirutaInformacion, "../problema6/informacion.txt")

mirutaDepartamento = os.path.abspath(os.path.dirname(__file__))
rutaDepartamento = os.path.join(mirutaDepartamento, "../problema6/departamento.txt")

mirutaBD = os.path.abspath(os.path.dirname(__file__))
rutaBD = os.path.join(mirutaBD, "../problema6/company.sql")

connection = sqlite3.connect(rutaBD)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Informacion(id INT, name TEXT, age INT, address TEXT, salary REAL, PRIMARY KEY (id))")
cursor.execute("CREATE TABLE IF NOT EXISTS Departamento(id INT, dept TEXT, emp_id INT, PRIMARY KEY (id))")

archivoInformacion = open(rutaInformacion, 'r')
contenidoInformacion = archivoInformacion.read()

archivoDepartamento = open(rutaDepartamento, 'r')
contenidoDepartamento = archivoDepartamento.read()

archivoInformacion.close()
archivoDepartamento.close()

rows1 = contenidoInformacion.split('\n')
rows1 = rows1[1:]
dataInformacion = [tuple(x.split()) for x in rows1]

rows2 = contenidoDepartamento.split('\n')
rows2 = rows2[1:]
dataDepartamento = [tuple(x.split(',')) for x in rows2]

cursor.executemany("INSERT INTO Informacion (id, name, age, address, salary) VALUES (?, ?, ?, ?, ?)", dataInformacion)
cursor.executemany("INSERT INTO Departamento (id, dept, emp_id) VALUES (?, ?, ?)", dataDepartamento)
connection.commit()

menor20k = 20000.0
cursor.execute("SELECT * FROM Informacion WHERE salary<?", (menor20k,))
print(cursor.fetchall())

connection.row_factory = lambda cursor, row: row[0]
c = connection.cursor()
edades = c.execute("SELECT age from Informacion").fetchall()

nombres = c.execute("SELECT name from Informacion").fetchall()
for word in nombres:
    if word[0].isupper():
        print(word)

sumaEdades = 0
for i in edades:
    sumaEdades = sumaEdades + i
promedio = sumaEdades/len(edades)
print("El promedio de las edades es: {:.2f}".format(promedio))

connection.close()


