#Arreglos similares a una lista
#SON INMUTABLES
#Son mas eiicientes que una lista 
#Usualmente usadas para variiables tmeporales (usar-borrar)


y=(2,5,6,3,9,0)
print(y)
#print(dir(y)) #funciones: count, index

#Asignaciones
#Izquiera a derecha:
(j,k)=(4,'Fredo')

print(j)
print(k)
print((j,k))

#Nota: sUna tupla se asemeja a un diccionario
#Las tuplas son comparables
#Se itera cada elemento con su contraparte y si se cumple la condicion, devuelve true
#si ningun elemento cumple la condicion regresa false
#Se cumple al encontrar el primer elemento
print((1,2,3)<(1,2,1))
print((2,8,1)>(2,7,9))


#ejercicio
#¿Que imprime el siguiente codigo?
#R:
d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)

print("Sguiente quest: Comparar y ordenar tuplas")
print("Continuara...")

#####################################################
# ################       METODOS     ##################
# count()   //Devuelve el numero de veces que se encuentra un objeto (lista.count(1))
# index(lista.index())  //Devuelve el indice o posicion de el elemento indicado