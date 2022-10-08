from sre_constants import SRE_FLAG_IGNORECASE
from turtle import clear

#Una funcion es una pieza de codigo que realiza una accion con o sin datos de entrada y devuelve algo
# Una funcion es reusable
#Existen dos tipos de funciones en ptyton:
#Propias (print(), input(), type()...)
#Defindas por el programador que usa despues (nuevas palabras reservadas)


#Definicion de funciones
def saludo():
    print("Hola mundo")

#max() devielve el valor que tenga mayor valor
#min() devuelve el elemento con el menos valor


#Funcion con parametros
def saludito(nombre):
    print("Hola", nombre)

nom="sergio"

saludo()
saludito(nom)

#retorno de valores
#usamos paalbra reservada return

def suma(a,b):
    return a+b

print(suma(3,89))


#una funcion que no devuelve un valor es una VOID FUNCTION
#una uncion que devuelve un valor es una FRUITUL

#NOTAS:
#-Parrafos que capturen una idea y nombralo
#-Si algo es complejo, dividelo en piezas mas pequeñas(funciones)
#-Haz librerias de de cosas que reutiilices constantemente


