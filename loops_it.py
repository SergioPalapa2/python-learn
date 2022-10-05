#loop WHILE

print("uso de loops e iteraciones")

x=10
while x>0:
    print(x)
    x=x-1

print("Fin de ciclo")

#un BREAK rompe el cclo en cuanto sea llamado

while True:
    line=input('> ')
    if line[0]=="#":
        continue
    if line=="done":
        break
    print(line)

print ("done")


#loops deindos
#FOR
#Un loop iterativo recorre los elementos de una serie de datos

for i in [4,3,2,1]:
    print(i)

print("blastof")