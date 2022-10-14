#Las listas y las cadenas son compatibles (mejores amigos :) )
#funcion split() //Separa una cadena y la devuelve como una lista, separa mediante los espacios

nombreC="Sergio Joaquin Palapa Osante"
print(nombreC)
nombreL=nombreC.split() #crea una lista a partir de la cadena

print(nombreL)

#Un split puede funcionar definiendo delimitadores.
#Pueden dividirse mediante , o ;

experiencia="Soporte;SoporteN1;Monitorista;Desarrollador"
print(experiencia)
exp=experiencia.split(";")
print(exp)

