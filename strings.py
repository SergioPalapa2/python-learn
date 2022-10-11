#Cadenas de texto
#Una cadena es una secuencia de caracteres
#Es posible concatenar straings con +
#Es posible convertir string de numeros a enteros mediante int()

str1="Hello!"
str2="there"

saludo=str1+str2 #concatenacion

print("Concatenado: ",saludo)
print("No concatenado: ",str1,str2)

str3='666'
#str3+5 //arrojara error ya que la variable no es del tipo entero
res=int(str3)+5 #conversion de cadena a numero
print(res)

#Buscando dentro de strings
#Es posible realizar una busqueda mediante notacion de brackets[]
#Arrojara error si se intenta indexar un valor mas alla del tamaño de la cadena

print(saludo[0]) #imprime la primera letra de la cadena (H)

#La funcion LEN nos regresa el tamaño en caracteres de una cadena
print("Tamano del saludo: ", len(saludo))


#Podemos utilizar la funcion len y un ciclo while para buscar en las posiciones de la cadena
fruta="melocoton"
index=0

#usando WHILE
while index<len(fruta):
    print(index+1, fruta[index])
    index=index+1
print("Fin del conteo")

#usando FOR (mas elegante :))
for letra in fruta:
    print(letra)









