#Funcion que incrementa el ultimo numero de un string
#Si no existe un nimero agrega un 1

#Expresiones regulares
#Cadenas
import re

#def increment_string(strng):

#print(increment_string('holad5454'))

strng="hola454545"
num=re.findall('[0-9]+$',strng)
tam=len(num[0])


print(strng)
print(num)
print(tam)




