class Coche():
	def __init__(self):  #Indica el constructor de una clase
		self.__largoChasis=250  #Propiedades
		self.__anchoChasis=120
		self.__ruedas=4  #se encapsula y no sera accesible desde fuera
		self.__enmarcha=False

	def arranca(self, estado):  #Comportamiento
		self.__enmarcha=estado

		if(self.__enmarcha==True):
			chequeo=self.__check()

		if(self.__enmarcha and chequeo):
			return "El coche esta en marcha"
		elif(self.__enmarcha and chequeo==False):
			return "Inicio interrumpido. Revise parametros de inicio"
		else:
			return "El coche esta parado"
	
	def estado(self):
		print("Coche con ", self.__ruedas, " ruedas")
		print("Largo de ", self.__largoChasis, " cm")
		print("Largo de ", self.__anchoChasis, " cm")



	def __check(self):
		print("Escaneo inicializado")
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False



print("Constructor de clases")

miCoche=Coche() #instanciar una clase
print(miCoche.arranca(True))
miCoche.estado()



miCoche2=Coche()
print(miCoche2.arranca(False))
miCoche2.estado()



