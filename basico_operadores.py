#Los operadores en pyton permiten manipular y comparar valores o variables 

#Operadores en python
# + (suma), - (resta), *(multiplicacion), /(divsion), **(potencia), %(residuo) 
print("Pagos")
bruto=input("Salario por hora: ") #Asignacion de una variable al valor de entrada por usuario
hours=input("Horas laboradas: ")


#int() <---funcion que devuelve un entero
#float() <---funcion que devuelve un flotante

bruto1=float(bruto)
hours1=float(hours)

payment=(bruto1*hours1)-(bruto1*0.16)
print("Pago correspondiente: ", payment)



