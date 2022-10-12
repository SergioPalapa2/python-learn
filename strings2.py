#Busqueda en strings por secciones
#Usamos : para definir un rango de busqueda
#Reglas:
#- El segundo valor no esta incluido
#- En caso de definir un segundo valor mas grande que la cadena solo terminara en el ultimo valor


nombre="Sergio Palapa"
print(nombre[0:6]) #Solo imprime desde posicion 0 a 5
#print(nombre+6) //no es posible concatenar cadenas con numeros


#El operador IN puede ser utilizado para saber si una cadena esta dentro de otra cadena
#Devolvera true o false (funciona como una sentencia if)

print("Palapa" in nombre) #Devuelve true
print("Palapo" in nombre) #Devuelve false

if "palapa" in nombre:
    print("Existe")
else:
    print("No existe")


#Python contiene varias funciones con las que operar cadenas
#estas funciones no modifican la cadena original, solo devuelven un nuevo valor

print("Manejo de funciones de cadena \n")
print(nombre.lower())
print("CASE".lower())
print(type(nombre))
print(dir(nombre)) #dir: lista de atributos validos del objeto

#librerias para strings
#str.capitalize()
#str.center(...)
#str.endswith(...)
#str.find(...)
#str.lstrip(...)
#str.replace(...)
#str.rstrip(...)
#str.strip(...)
#str.upper(...)


#Busqueda en strings
#Usamos find() para buscar subcadenas en una cadena mayor
#devuelve la posicion en donde inicia la coincidencia
#Encuentra la primer coincidencia
#Si la cadena no es encontrada devuelve -1
boleta="2012350653"
print(boleta.find("2012"))
print(boleta.find("3"))
#Por default comienza la busqueda en el indice 0
#Se puede indicar el inicio de la busqueda colocando el indice como segundo argumento, ej cadena.find("A",5)
#Se puede indicar hasta donde se puede realizar la busqueda, colocando un tercer argumento, ej cadena.find("A",5,10)




#Mayusculas y minusculas
#Para convertir el tamaño de la letra usamos lower() o upper()
curp="PAOSOFVOF"
print(curp.lower())



#Sustitucion
#Para busqueda y sustitucion  usamos la funcion replace()
#Rempleza todas las coincidencias de una cadena
greet="Hola bob"
newstr=greet.replace('bob','rob')
print(newstr)




#Manipulacion del espacio en blanco
#lstrip() remueve el espacio por la izquierda
#rstrip() remueve el espacio por la derecha
#strip() remueve ambos espacios, al inicio y al final

cadena2="  sergio  "
print(cadena2)
print(cadena2.lstrip())
print(cadena2.rstrip())


#Prefijos
#Es posible verificar si una cadena inicia con algun caracter o cadena
#Devuelve true o false en caso de cumplirse 
line="Porfavor mantenga la calma"
print(line.startswith('P'))
print(line.startswith('M'))


#Parseo y extraccion
#Se pueden combinar las tecnicas anteriores para realizar una revision exhaustiva y extraccion de informacion

#Ejemplo: Extraer el dominio de la cadena
data="From stephen.marqard@uct.ac.za Sat Jan 5 09:14:23 2022"
print(data)
arrpos=data.find("@") #encontramos la posicion del @
print("Posicion de @ en:",arrpos)
sppos=data.find(" ",arrpos) #encontramos la posicion del espacio despues del arroba
print("Posicion del espacio en:",sppos) 
host=data[arrpos+1:sppos]
print("El host es:", host)



#NOTA: En python 3 todas las cadenas con UNICODE













