#Ciclo de vida de un objeto
#Los objetos son CREADOS-USADOS-DESCARTADOS
#Usamos constructores y destructores

class partyAnimal:
    x=0
    def __init__(self):
        print("Party constructed")

    def party(self):
        self.x=self.x+2
        print("So far", self.x)
    
    def __del__(self):
        print("Party destructed", self.x)

an=partyAnimal() #Objeto construido

an.party()
an.party()

an=42 #Objeto asignado a an destruido
print('An ahora contiene', an)


#Los constructores pueden tener parametros adicionales
#Normalmente usados para inicializar variables para una instancia en particular de la clase

class partyAnimal2:
    x=0
    name=""
    def __init__(self,z): #se envia valor de inicializacion
        self.name=z
        print(self.name,"created")

    def party(self):
        self.x=self.x+2
        print(self.name,"conteo", self.x)
    
    def __del__(self):
        print("Party destructed", self.x)


s=partyAnimal2("Sally") #el valor se envia al constructor
s.party()

j=partyAnimal2("Jimbo")
j.party()


s.party()