#Jhoan de Leon
#Ricky Chan
#Deepak Wadhwani
def temperatura_fahrenheit(tempc):
  return (9 / 5) * tempc + 32

def temperatura_celsius(tempf):
  return (5 / 9) * (tempf - 32)

temperatura =float(input("Ingresa una temperatura: "))
conversion =input("¿Desea convertir este valor hacia grados (F)ahrenheit o (C)elsius? ").upper()

if conversion == "C":
  print("La temperatura ", str(temperatura) +" F equivale a", str(temperatura_celsius(temperatura)) + " C")
elif conversion == "F":
  print("La temperatura ", str(temperatura) + "C equivale a", str(temperatura_fahrenheit(temperatura))+ " F")
else: 
  print("Debe introducir C o F")