import math #Libreria matematica
import sys #Libreria de sistema
class Puntos:
    def __init__(self, x, y): #Constructor
        self.x = x
        self.y = y

    def DistanciaEuclidiana(self, punto_2): #Calculo en base a otro punto
        try:
            d = math.sqrt(math.pow(punto_2.x - self.x, 2) + math.pow(punto_2.y - self.y, 2))
            return d
        except Exception as e:
            print("A ocurrido un error ", e.__class__)
            exit(1)

punto_1 = Puntos(1.5,2.3)
punto_2 = Puntos(2,3)
distancia = punto_1.DistanciaEuclidiana(punto_2)
print("La distancia Euclidiana es: ", distancia)


