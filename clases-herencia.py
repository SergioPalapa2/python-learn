#HERENCIA: Crear una nueva clase, extendiendo una ya existente
#Clase original = Padre
#Clase resultante = hijo
 
class grupoAnimal():
    x=0 

    def __init__(self): 
        print("Objeto construido")

    def __del__(self): #el parametro self del contructor apunta a la instancia del objeto y a parametros adicionales
        print("Objeto destruido", self.x)
    

    def grupo(self): #metodo
        self.x=self.x+1
        print("Hasta ahora: ", self.x)









