#Diccionarios y loops(ciclos)
# Ejercicio: Conteo de palabras (aplicar split y llevar un conteo de cada palabra independiente)
count=dict()
string=input("Escribe tu texto:")
words=string.split()
print("Palabras:", words)

for word in words:
    count[word]=count.get(word,0)+1
print(count)

#Es posible iterar en un diccionario y obtener sus key y el valor del key
for key in count:
    print(key,count[key])


print(list(count)) #metodo list() nos regresa un listado de los keys
print(count.keys()) #metodo keys() nos regresa los keys 
print(count.values()) #metodo values() nos regresa los valores de cada key
print(count.items()) #metodo que devuelve key y valor en tuplas (en breve...)

#Iteracion con dos variables
for aaa,bbb in count.items():
    print("item",aaa,bbb)
