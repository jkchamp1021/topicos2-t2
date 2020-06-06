import math #Libreria matematica
import sys #Libreria de sistema
import csv #Libreria CSV reader/writter
import time #Libreria de tiempo
ARG_NUM = 0 #Argumentos Permitidos
DELAY_PRINT = 0.5  #Delay de calculo e impresion
class Puntos:
    def __init__(self, x, y): #Constructor
        self.x = x
        self.y = y

    def DistanciaEuclidiana(self, punto_2): #Calculo en base a otro punto
        try:
            d = math.sqrt(math.pow(punto_2.x - self.x, 2) + math.pow(punto_2.y - self.y, 2))
            return d
        except Exception as e:
            print("A ocurrido un error: {}\n\n".format(e.__class__))
            exit(1)
def VerifyArg(): #Numero adecuado de argumentos
    return True if(len(sys.argv) - 1 == ARG_NUM) else False

archivo = "euclid.csv" if(VerifyArg()) else sys.argv[1]

with open(archivo,'rU') as csvf:
    csv_archivo = csv.reader(csvf, delimiter=',', dialect=csv.excel_tab)
    lineas = 0
    for row in csv_archivo:
        if not lineas == 0:
            punto_1 = Puntos(float(row[0]), float(row[1]))
            punto_2 = Puntos(float(row[2]), float(row[3]))
            distancia = punto_1.DistanciaEuclidiana(punto_2)
            print("Punto 1 [{} , {}] - Punto 2 [{} , {}] - La distancia Euclidiana es: {}\n\n\n".format(punto_1.x,punto_1.y,punto_2.x,punto_2.y,distancia))
            #time.sleep(DELAY_PRINT)
        lineas += 1
    print("Calculado un total de {} lineas".format(lineas-1))


