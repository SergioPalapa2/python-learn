from datetime import datetime #libreria que pregunta la hora al sistema

class perro(): #plantilla para crear perro
    #atributos
    ojos=2
    patas=4
    cola=1
    nariz=1
    orejas=2
    nombre=""
    fecha=""
    sexo=""
    color=""
    fecha_nac=""
    def __init__(self):
        print("Nuevo perro")

    def ladrido(self):
        print("Perrito dice guau guau")

    def nombrar(self,nom):
        self.nombre=nom
        print("Nombre:", nom)


class chihuahua(perro): #plantilla que crea un chihuahua heredando de perro 
    tamaño="mini"

    def __init__(self):
        print("Nuevo perro chihuahua")
        fecha_nac=datetime.now()
        print("Nacido en ", fecha_nac)

    def ladridoCh(self):
        print("wawawawawawawawawawawawawa")


class doberman(perro):  #plantilla para perro doberman
    tamaño="medio-grande"
    def __init__(self):
        print("Nuevo perro doberman")
    def ladridoD(self):
        print("bark bark bark bark")

celdas=[] #se declara la variable de celda

def perrera(perro):
    celdas.append(perro)

#main
perro1=perro() #nuevo objeto perro
perro1.nombrar("Perro prueba1")
print(perro1.ladrido())



perro_chih=chihuahua()#nuevo objeto chihuahua
print("Patas:",perro_chih.patas)
print("Ojos",perro_chih.ojos)
print("Tamaño:",perro_chih.tamaño)
perro_chih.nombrar("Nachito")
perro_chih.ladridoCh()
#perro_chih.ladrido()
perro_chih.sexo="M"
print("El sexo del perro es: ",perro_chih.sexo)



perro_d=doberman()
print(perro_d.ladridoD())




perrera(perro1)
perrera(perro_chih)
perrera("perro desconocido")

for perrito in celdas:
    print("Celda ", perrito)

print(perro1)