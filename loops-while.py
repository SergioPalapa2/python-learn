#WHILE
#Ciclo que se ejecuta mientras una condicon inicial sea verdadera
#Contiene variables de iteracion qu pueden cambiar durante la ejecucion del loop

print("Uso de cliclo while")

x=10

while x>0: #mientras x sea mayor que 0 se ejecutara el codigo dentro del while
    print(x)
    x=x-1
    print("Fin de iteracion")
print("Fin del cliclo")


#Un BREAK rompe el ciclo en cuanto sea llamado

print("#: continua")
print("done: finaliza")

while True:
    line=input('> ')
    if line[0]=="#":
        continue
    if line=="done":
        break
    print(line)

print ("Finalizaste el programa guapo")


