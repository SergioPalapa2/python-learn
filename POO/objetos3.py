#Herencia
#Creacion de una nueva clase utilizando codigo de una clase ya creada
#Clase original: Padre
#Clase nueva: hijo

class partyAnimal:
    x=0
    name=""
    def __init__(self,nam):
        self.name=nam
        print(self.name,"constructed")


    def party(self):
        self.x=self.x+2
        print("So far", self.x)
    
    def __del__(self):
        print("Party destructed", self.x)


class footballFan(partyAnimal): #Hereda propiedades de partyAnimal
    points=0
    def touchdown(self):
        self.points=self.points+7
        self.party()
        print(self.name,"points",self.points)


s=partyAnimal("Serch")
s.party() #metodo de la clase original

j=footballFan("Jim")
j.party()
j.touchdown()

