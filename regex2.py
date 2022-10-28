#Expresiones regulares
#Igualacion y extraccion de datos
import re

#Busca cadenas que contengan los digitos 0-9
string='ingles: 80, aleman: 90, ruso: 20'
x=re.findall('[0-9]+',string) #uno o mas digitos
print(x)

#Busca coincidencias con las letras
y=re.findall('[aeiou]+',string) #Retorna [] ya que no existen letras mayusculas
print(y)


#Greedy matching (usa la cadena mas larga)
string2='From: using : character'
match=re.findall('^F.+:', string2)
print(match)


#Non greedy matching (usa la cadena mas corta encontrada)
match2=re.findall('^F.+?:', string2)
print(match2)


