#OBJETO: Pieza de codigo que realiza algo
#Contiene atributos y metodos


class grupoAnimal():#la palabra class crea la "plantilla"
    x=0 #atrbuto
    
    #Ciclo de vida del objeto
    #Generalmente el metodo __init__ es usado para inicializar valores
    #es relativamente raro necesitar un destructor

    def __init__(self): #Metodo especial para controlar que pasa en la creacion
        print("Objeto construido")

    def __del__(self): #Metodo especial para controlar que pasa en la destruccion
        print("Objeto destruido", self.x)
    


    def grupo(self): #metodo
        self.x=self.x+1
        print("Hasta ahora: ", self.x)


#Invocacion de la clase
an=grupoAnimal() #construccion del objeto o instanciia de la clase
an.grupo()#llamada al metodo
an.grupo()
an.grupo()
grupoAnimal.grupo(an)

#tipos
print("type ",type(an))
print("dir", dir(an))
print("type x", type(an.x))
print("type grupo ",type(an.grupo))

Print("Siguiente camino: Instancias Multiiples")