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


#Forma de extraer informacion separando la porcion que sera extraida, usando ()
string3="From stephen.marquard@uct.ac.za Sat Jan 5 09:14:26 2012"
match3=re.findall('\S+@\S+',string3)
print(match3)
#usando ()
matchb=re.findall('^From (\S+@\S+)',string3)
print(matchb)


#ejercicio
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)


