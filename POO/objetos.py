#Programacion orientada a objetos

# Programa minimo
# input ---> [proceso]---->Salida

#Procesamiento de informacion
inp=input("Europe floor?")
usf=int(inp)+1
print("US floor:", usf)

#Objetos
#Un programa puede estar compuesto por varios objetos que interactuan entre si
#Un objeto es un trozo de codigo contenido en si mismo
#Los objetos tienen limites, lo cual permite solo enfocarse en como se usa determinado objeto

#Definiciones
#class: Una plantilla
#Metodo: Funcionalidad definida de una clase
#Atributo: Datos en la clase
#Instancia: Uso particular de una clase

class partyAnimal:
    x=0
    def party(self):
        self.x=self.x+1
        print("So far", self.x)
    

an=partyAnimal()

an.party()
an.party()
an.party()


#dir() //Encontrar los metodos asociados a un objeto
# con _ son usados por python mismo

print(type(an)) #dir es similar a typer. Se indica "algo" de un objeto
print(dir(an))

