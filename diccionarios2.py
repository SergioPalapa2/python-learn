#Aplicaciones de los diccionarios
#Un uso muy recuente para los diccionarios son los histogramas
#muestras que indican la cantidad o frecuencia de algo

names=dict()
names["sergio"]=1
names["Fernando"]=1
names["sergio"]=names["sergio"]+1
names["sergio"]=names["sergio"]+4
print(names)

#Usamos el operador IN para saber si existe el indice en un diccionaro
print("omar" in names)


#si se tiene un nombre nuevo es añadido a la lista
#Si ya se tienen ocurrencias, el cnotador aumenta
#Codigo del HISTOGRAMA
count=dict()
lista=['liz','serch','lizeth','serch','chen','liv','liz','ana','liz']
for name in lista:
    if name not in count:
        count[name]=1
    else:
        count[name]=count[name]+1

print(count)


#El metodo GET valida si existe algun indice(key) en un diccionario y regresa su valor
#x=dict.get(name,0) <---args:key, default

count2=dict()
for name in lista:
    count2[name]=count2.get(name,0)+1 #sustituye el condicional en una sola linea

print(count2)



