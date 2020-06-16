import collections
import string
import os.path

def obtenerMensaje():
    miRuta = os.path.abspath(os.path.dirname(__file__))
    ruta = os.path.join(miRuta, "../problema2/encriptado.txt")
    archivo = open(ruta,'r', encoding='utf-8')
    return archivo.read()

def descifrarMensaje(mensaje, desplazamiento):
    alfabetoEspMayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    alfabetoEspMiniscula = "abcdefghijklmnñopqrstuvwxyz"

    mayuscula = collections.deque(alfabetoEspMayuscula)
    miniscula = collections.deque(alfabetoEspMiniscula)

    mayuscula.rotate(-desplazamiento)
    miniscula.rotate(-desplazamiento)

    mayuscula = ''.join(list(mayuscula))
    miniscula = ''.join(list(miniscula))

    transTabMayuscula = str.maketrans(alfabetoEspMayuscula, mayuscula)
    transTabMiniscula = str.maketrans(alfabetoEspMiniscula, miniscula)
    
    return mensaje.translate(transTabMayuscula).translate(transTabMiniscula)

mensaje = obtenerMensaje()

for i in range(27):
    print("Desplazamiento", i,"\n",descifrarMensaje(mensaje, i),"\n")



    


