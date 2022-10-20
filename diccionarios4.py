#Manejando archivos
print("Archivos")

#abriendo archivo
nombre=input("Nombre del archivo: ")
manejador=open(nombre)


counts=dict()
for line in manejador: #iteracion en cada linea del archivo
    #print(line)
    words=line.split()
    for word in words: #iteracion de cada palabra en la linea actual
        counts[word]=counts.get(word,0)+1
print(counts) #histograma

#Encuentra la palabara mas comun y el conteo mas grande
bigCount=None
bigWord=None
for word,count in counts.items():
    if bigCount is None or count>bigCount:
        bigWord=word
        bigCount=count
print(bigWord, bigCount)



# #Ejercicio
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])

