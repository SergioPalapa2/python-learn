#FOR
#El ciclo for es un ciclo ya definido mediante una variable contador
#Un loop iterativo recorre los elementos de una serie de datos

for i in [4,3,2,1]:
    print(i)
print("blastof")



#Ejemplo1
friends=['Carlos','Jenna','Marco','Kamus']
for friend in friends:
    print('Happy new year ', friend)

print(friend)#La variable es creada y existe en el entorno fuera del FOR
print('Done!')



#Ejemplo2
#Cual es el numero mayor?
array=[3,4,9,22,31,9,1,3]
mayor=-1 #variable inicializada

for f in array:
    if f>mayor:
        mayor=f #si el numero en el array es mayor, lo almacena
    else:
        continue
print('El mayor es', mayor)




#Ciclo con un contador
count=0
for numero in [20,21,22,23,24,25,26,27,28,29]:
    count=count+1 #el contador mantiene el control de las posiciones
    print('posicion',count,' elemento', numero)


#Ejemplo3
#Encontrar el promedio de una serie de valores
calif=[10,6,7,10,9,6,4,8]
conteo=0
suma=0

for cal in calif:
    conteo=conteo+1
    suma=suma+cal

print("El promedio es", suma/conteo)


#python contiene los operadores:
#is (similar a ==)
#is not
#Devuelven false o true











