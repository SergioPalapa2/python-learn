#Palabra mas usada en un archvo

#Diccionarios
#Tuplas
#sort()

fhandler=open('file_ejj.txt') #Abre el archivo y lo asigna a un manejador

counts=dict()
for line in fhandler:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0) +1 #Idiom para conteo 

lst=list()
for k,v in counts.items():
    newTup=(v,k)
    lst.append(newTup)

lst=sorted(lst,reverse=True)
for v,k in lst[:len(lst)]:
    print(k,v)
print('#####################')

print(sorted([(v,k) for k,v in counts.items()])) # Version reducida del algoritmo de ordenamiento


