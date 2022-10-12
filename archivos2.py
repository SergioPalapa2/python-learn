#El manejador de archivos puede visualizarse como una secuencia de cadenas
#Podemos usar el ciclo FOR para iterar a traves del manejador

manejador=open('prueba_doc.txt')
print(manejador)
c=0

for linea in manejador:
    c=c+1
    print('linea:',c)
    print(linea)#Imprime cada linea en el archivo

#Nota: solo permite usar el manejador una vez¿?

#texto=manejador.read()
#print("Tamaño total:", len(texto))



#Busqueda a traves de un archivo
fileo=open("file1.txt")
for linea in fileo:
    if linea.startswith("Nombre"):
        print(linea)


#5:27
#Continuara...
print("Continuara...")
        

