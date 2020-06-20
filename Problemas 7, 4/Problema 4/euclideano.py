import math #Libreria matematica
import sys #Libreria de sistema
import csv #Libreria CSV reader/writter
import time #Libreria de tiempo
ARG_NUM = 0 #Argumentos Permitidos
DELAY_PRINT = 0.1  #Delay de calculo e impresion
class Puntos:
    def __init__(self, x, y): #Constructor
        self.x = x
        self.y = y

    def distanciaEuclidiana(self, punto_2): #Calculo en base a otro punto
        try:
            d = math.sqrt(math.pow(punto_2.x - self.x, 2) + math.pow(punto_2.y - self.y, 2))
            return d
        except Exception as e:
            print("A ocurrido un error: {}\n\n".format(e.__class__))
            exit(1)
def verifyArg(): #Numero adecuado de argumentos
    return True if(len(sys.argv) - 1 == ARG_NUM) else False

def bresenham( punto_a, punto_b ): #Calculo del trayectoria de linea - Algoritmo de Bresenham
    #Delta Y, Delta X, Delta error
    dy = int(punto_b.y ) - int( punto_a.y )
    dx = int( punto_b.x ) - int( punto_a.x )
    sx = 1 if( punto_a.x < punto_b.x ) else -1
    sy = 1 if( punto_a.y < punto_b.y ) else -1
    err = dx + dy 
    x, y = int(punto_a.x), int(punto_a.y)
    err_2 = 0
    while True:
        time.sleep(DELAY_PRINT)
        if ( x == punto_b.x and y == punto_b.y): break
        err_2 = err * 2
        if(err_2 >= dy):
            err -= dy
            x += sx

        if(err_2 <= dx):
            err += dx
            y = y + sy
        print("{} , {}, - {} <= {} aumenta y en y - {} >= {} aumenta x".format(x,y, err_2,dx,err_2,dy))

archivo = "euclid.csv" if(verifyArg()) else sys.argv[1]

with open(archivo,'rU') as csv_archivo:
    csv_data = csv.reader(csv_archivo, delimiter=',', dialect=csv.excel_tab)
    lineas = 0
    for row in csv_data:
        if not lineas == 0:
            punto_1 = Puntos(float(row[0]), float(row[1]))
            punto_2 = Puntos(float(row[2]), float(row[3]))
            distancia = punto_1.distanciaEuclidiana(punto_2)
            print("Punto 1 [{} , {}] - Punto 2 [{} , {}] - La distancia Euclidiana es: {}\n\n\n".format(punto_1.x,punto_1.y,punto_2.x,punto_2.y,distancia))
            if(lineas > 0  and lineas < 11): bresenham(punto_1, punto_2)
            #time.sleep(DELAY_PRINT)
        lineas += 1
    print("Calculado un total de {} lineas".format(lineas-1))


