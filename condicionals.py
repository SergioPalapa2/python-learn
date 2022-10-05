#comparadores
# < > >= <= == !=

#condicional
x=10
y=25

if y>x:
    print("el valor de y es mayor que x, muy bien hermoso")


#multi ways (else)

#boleta=2025
#if boleta==2025:
#    print("Procede inscripcion")
#else:  print("Acude a comison de stuacion escolar")


#elif permite seleccionar solo una opcion y terminar el bloque

c=10

if c<9:
    print("mayor")
elif c==10:
    print("es iigual")


# try y except como orma de compensar errores de ejecucion

val="hola python"
try:
    int(val)
except:
    val=-1

if val>=0:
    print("Valor numeroico")
else:
    print("No numerico")    

