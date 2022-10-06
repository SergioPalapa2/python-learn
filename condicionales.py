#Comparadores
# < > >= <= == !=

x=10
y=25

if y>x: #condicional IF
    print("el valor de y es mayor que x, muy bien hermoso \n")

print("Continuamos -------> \n")

#En caso de haber mas de una condicion usamos ELSE
boleta="2015"
if int(boleta) >= 2015: #funcion INT convierte el valor str en int, siempre y cuando sea numero
    print("Procede inscripcion")
else:  print("Acude a comison de stuacion escolar")


#ELIF permite seleccionar solo una opcion y terminar el bloque

c=10
if c<9:
    print("mayor")
elif c==10:
    print("es igual")


# try y except como forma de compensar errores de ejecucion

val="hola python"
try:
    int(val)
except:
    val=-1

if val>=0:
    print("Valor numerico")
else:
    print("No numerico")    

