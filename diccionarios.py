#Diccionarios
#Un diccionario es un contenedor que organiza elementos mediante un id o key

#lista: coleccion lineal y ordenada
#diccionario: Conjunto de elementos con su propia etiqueta

from wsgiref.validate import validator


diccionario=dict() #funcion que crea un diccionario vacio
diccionario['edad']=23
diccionario['mes']="septembre"
diccionario['año']=1992
diccionario['entidad']="34"



print(diccionario)
print(diccionario['edad'])

#La dierencia principal entre un diccionario y una lista es su tipo de indexado

#Diccionario de constantes
#Se usa con {}
ooo={}
print (ooo)


dict = {"Fri": 20, "Thu": 6, "Sat": 1}
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9

print(dict)


#####################################################
################       METODOS     ##################
# len()
# del dicc[k] //Elimina el objeto seleciconado
# k in dicc  //Devuelve true si existe el objeto en el diccionario
# dicc.keys()  //Devuelve todas la claves del diccionario
# dicc.values()  //Devuelve todos los valores del diccionario
# dicc.items()  //Devuelve la tupla clave-valor
# dicc.clear()  //Borra todos los items del diccionario
# dicc.copy()  //Devuelve la copia del diccionario
# dicc2.upate(dicc)  //Fusiona las entradas de de dicc2 en dicc
# dicc.popitem()  //Devuelve y elimina un par arbitrario clave-validator








