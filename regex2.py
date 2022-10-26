#Expresiones regulares
#Igualacion y extraccion de datos
import re

string='ingles: 80, aleman: 90, ruso: 20'
x=re.findall('[0-9]+',string)
print(x)

y=re.findall('[aeiou]+',string) #Retorna [] ya que no existen letras mayusculas
print(y)

print("Continuando....")
