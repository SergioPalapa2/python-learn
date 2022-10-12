#Manejo de archivos
#Un archivo puede considerarse una secuencia de lineas almacenadas en la computadora
# 1 Indicar a python que archivo vamos a usar
# 2 Indicar a python que haremos con el

#La funcion open() regresa un "manejador de archivos"
#Variable usada para realizar acciones sobre el archivo

#handle=open(filename,mode)
#ejemplo fhand=open('file.txt','r')
#Regresa una variable manejador del archivo
#EL modo es opcional
#r si se leera el archivo
#w si se escribira en el archivo

fhand=open('prueba_doc.txt')
print(fhand)

#Se agrega una nueva linea en una cadena con \n
linea="Sergio\nPalapa"
print(linea)
print("Tamaño:",len(linea))#Se toma como un caracter



