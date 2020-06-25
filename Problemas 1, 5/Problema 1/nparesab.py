#Jhoan de León
#Ricky Chan
#Deepak Wadhwani

import sys

numero_uno = int(sys.argv[1])
numero_dos = int(sys.argv[2])

def pares(lower, upper):
  print("Los numeros par entre " + str(lower) + " y " + str(upper) + " son: ")
  for i in range(lower, upper + 1):
    if ( i % 2 == 0):
      print(i)


if numero_uno >= numero_dos:
  print("El numero uno debe ser menor que el numero dos")
else:
   pares(numero_uno, numero_dos)