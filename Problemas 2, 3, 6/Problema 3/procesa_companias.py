import os.path

miRuta1 = os.path.abspath(os.path.dirname(__file__))
ruta1 = os.path.join(miRuta1, "../problema3/compania.txt")

miRuta2 = os.path.abspath(os.path.dirname(__file__))
ruta2 = os.path.join(miRuta2, "../problema3/nombres.txt")

def numLineas(ruta):
    with open(ruta) as archivoCompania:
        for i, l in enumerate(archivoCompania):
            pass
        return i + 1

def corporaciones(ruta,lineasCantidad):
    with open(ruta) as archivoCompania:
        for i in range(lineasCantidad):
            linea = next(archivoCompania).strip()
            if ("Incorporated" in linea or "Corporation" in linea or "Corp." in linea or "Inc." in linea):
                print(linea)
    
def head(ruta,lineasCantidad):
    with open(ruta) as archivoCompania:
        for i in range(lineasCantidad):
            linea = next(archivoCompania).strip()
            print(linea)


def imprimirCompaniasNombres(ruta1, ruta2):
    with open(ruta1) as archivoCompania, open(ruta2) as archivoNombres:
        for i in range(numLineas(ruta1)):
            linea1 = next(archivoCompania).strip()
            linea2 = next(archivoNombres).strip()               
            print(linea2,"-",linea1)
            
print("Número total de líneas en el archivo compania.txt:",numLineas(ruta1))

print("\nNombre de compañías que fueron registradas como corporaciones:")
corporaciones(ruta1,numLineas(ruta1))

print("\nIngrese cuantas líneas del archivo compania.txt desea ver:")
lineasCantidad = int(input())
head(ruta1,lineasCantidad)

print("\nImpresión de cada línea del archivo nombres.txt junto a cada línea del archivo compañia.txt:")
imprimirCompaniasNombres(ruta1,ruta2)

