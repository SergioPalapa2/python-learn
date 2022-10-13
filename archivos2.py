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

#Notas:
#- Podemos usar la funcion rstrip() para quitar nuevas lineas vacias
#- O mediante if not line.startswith(): continue
cvhandler=open("file2.txt")
for linea in cvhandler:
    linea=linea.rstrip()
    print(linea) #Imprime las lineas pero separadas por un espacio



#Usamos IN para realizar busquedas
cvhandler2=open("file2.txt")
for linea in cvhandler2:
    linea=linea.rstrip()
    if not 'Diseno' in linea:
        continue #finaliza el loop en curso y pasa al siguiente
    print(linea) 



