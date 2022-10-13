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

