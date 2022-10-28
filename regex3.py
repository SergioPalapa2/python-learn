#Expresiones regulares (regex)
#Aplicaciones practicas
import re

#Extraccion de texto usando find() y split()

#find()
data="From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos=data.find('@')
print(atpos)
sspos=data.find(' ',atpos) #conteo comienza desde la posicion atpos(21)
print(sspos)
host=data[atpos+1:sspos]
print (host)

#split()
words=data.split()
email=words[1]
pieces=email.split('@')
print(pieces[1])

#Usando EXPRESIONES REGULARES
rehost=re.findall('@([^ ]*)',data)  #[^ ] ==> hace match con caracteres no vacios
print(rehost)


#Escapar el caracter
message="Importe recibido: $100 para material"
cant=re.findall('\$[0-9.]+',message)  #escapamos el caracter con \
print(cant)


