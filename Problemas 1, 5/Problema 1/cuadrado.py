#Jhoan de León
#Ricky Chan
#Deepak Wadhwani

Lista = list()
for idx in range(5):
    temp = int(input("Ingrese el valor {:d}: ".format(idx + 1)))
    Lista.append(temp)

#Imprimir los numeros ingresados
print("\n\nLos Numeros Ingresados son: ")
for idx in range(5):
    print("El Valor {:d} es: {:d}" .format(idx + 1, Lista[idx]))

#Elimino los elementos repetidos de la lista
NuevaLista = list(set(Lista))

#Imprimir el valor con su Respuesta elevada al cuadrado
print("\n\nLos cuadrados de los numeros ingresados son:")
for idx in range(len(NuevaLista)):
    print("Valor {:d} es: {:d} y su Cuadrado es: {:d}".format(idx + 1 , NuevaLista[idx], pow(NuevaLista[idx],2)))