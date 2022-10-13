#Manejo de archivos mediante input
#El nombre del archivo se convierte en una variable

fnombre=input("Introduce el archivo a cargar: ")
try:
    fhand=open(fnombre)
except:
    print("Archivo incorrecto")
    quit()
    
for line in fhand:
    line=line.rstrip()
    print(line)
