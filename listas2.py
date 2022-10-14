#LISTAS

#Concatenacion
#es posible crear una nueva lista concatenando dos existentes
# Operador +

a=[2,4,6,8]
b=[1,3,5,7]

c=a+b
print(c)

#Las listas pueden ser separadas utilizando :
print(c[1:6]) #solo mostrara del indice 1 al 5

print(type(c))
print(dir(c))

#Podemos crear una lista mediante:
# lista=[]
# lista=list()  //funcion especifica
# append()  //agregar elementos a una lista

inventario=list()
inventario.append("PC2")
inventario.append("Monitor 2")
inventario.append("PC2")
inventario.append("monitor2")
inventario.append("Servidor 46")
inventario.append("monedero 23")

print(inventario)

# validar si existe algo en una lista, operador IN
# Devuelve true o false

print("servidor" in inventario) #devuelve false
print("Servidor 46" in inventario) #devuelve true


# ordenar una lista
# Usamos el metodo sort()

inventario.sort() #devuelve una lista ordenada alfabeticamente
print(inventario) 



#Funciones para operar listas
#len() //tamaño
#max() //tamaño
#min() //tamaño
#sum() //tamaño

cal=list()
cal=[7,10,9,5,8,10,9]

#Una forma de sustituir loops
print("Materias evaluadas:",len(cal))
print("Mayor calificacion:",max(cal))
print("Menor calificacion:",min(cal))
print("Promedio final:",sum(cal)/len(cal))








