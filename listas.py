#LISTAS
#Una lista es una coleccion de que contiene multiples valores en una sola variable
#Una lista puede contener cualquier objeto python, incluyendo otra lista
# Las listas son accesibles con sus indices []

troncoc=["Quimica", "Fisica", "Humanidades", "Programacion"]
matematicas=['Calculo diferencial', 'Calculo integral', 'Matematicas discretas', 'Algebra lineal']
computacion1=['POO', 'Circuitos logicos', 'Electronica analogica']

materias=[troncoc, matematicas, computacion1]
print(materias)

c=0
for mat in troncoc:
    print(mat)
    
#Las listas son mmodificables, accesando mediante su indice
troncoc[0]='Algebra'
print (troncoc)

#Tamaño de una lista
print(len(troncoc))

#Funcion range()
#Crea una secuencia de numeros iniciando por default en 0, incrementandose en 1, parando en el numero especificado
#Usualmente se usan para crear loops
#sintaxis: range(start, stop, step)
rango=(range(6))
print(rango)



#Definiciones
#Algoritmo: conjunto de reglas usadas para resolver un problema
#Estructuras de datos: Formas de organizar datos en una computadora




#####################################################
################       METODOS     ##################
# lista.append(item) //agrega el elemento al final de la lista
# lista.count(item)  //realiza el conteo del numero de veces que aparece un elementos
# lista.extend(lista)  //realiza un duplicado de la lista
# lista.index(item,inicio,final)  //Devuelve el indice del elemento, devuelve el primero que encuenta o si se encuentra en el rango especificado
# lista.insert(indice, item)  //se agrega un elemento en el indice indicado
# lista.pop() //devuelve y elimina el item situado mas a la derecha (contrario a append), es posible pasar como argumento un indice
# lista.remove() //elimina el primer item de la lista
# lista.reverse()  //invierte el orden de los items
# lista.sort()  //ordena de menor a mayor los items de la lista
# lista.clear()  //elimina los elementos de una lista y la devuelve vacia
# lista.copy()  //Devuelve una copia simple (equivale a lista(:))




