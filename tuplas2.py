#Ordenamiento y cmparacion de TUPLAS

#Ordenamos usando la posibilidad de ordenar una lista de tuplas para obtener una version ordenada del diccionario
d={'Monitores':8, 'CPU':6, "Mother":3, 'Arduinos':5, 'Billeteros':6}
print(d.items())
print(sorted(d.items())) #Metodo Sorted() //Ordena una lista

#Ordenamiento pos valores 
tmp=list()
for k,v in d.items():
    tmp.append((v,k)) #genera una lista "temporal" con cada tupla k-v

print(tmp)
print(sorted(tmp, reverse=True)) #Ordena de forma ascendente
print(tmp[0])




