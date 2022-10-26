#Expresiones regulares
#Provee patrones que permiten realizar busquedas inteligentes

#Quick guide 
# ^ linux: ctrl+shift+u ==> 5e
# \ linux: ctrl+shift+u ==> 5c

# ^       iguala el inicio de una linea
# $       iguala el final de una linea
# .       iguala cualquier caracter
# \s      iguala el espacio en blanco
# \S      iguala cualquier caracter que no sea espacio en blanco
# *       Repite un caracter cero o mas veces
# *?      Repite un caracter cero o mas veces (non-greedy)??
# +       Repite un caracter una o mas veces
# +?      Repite un caracter una o mas veces (non.greedy)
# []      Iguala un solo caracter en el listado
# [^XYZ]  Iguala un solo caracter no en el listado
# [a-z0-9] El set de caracteres puede incluir rangos
# (       Indica donde empezara la extraccion de caracteres
# )       Indica donde acabara la extraccion de caracteres



#Importar libreria re (import re)
#re.search() //Busca si una cadena coincide con una expresion regular
#re.findall()  //Extrae porciones de una cadena que coincidan con una expresion regular

import re

manejador= open('prueba_doc.txt')
for line in manejador:
    line=line.rstrip()
    if re.search('^Nombre',line): #Si la linea empieza con Nombre
        print(line)



