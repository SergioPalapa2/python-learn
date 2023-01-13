#Funcion que recibe una lista de cadenas que representan problemas aritmeticos.
#Regresa las operaciones acomodadas de forma vertical, una a lado de otra.
#Toma un segunda argumento, si es "true" se mostrara el resultado.

#Errores
#TODO: "Error: To many problems." si hay mas de 5 operaciones.
#TODO: "Error: Operator must be '+' or '-'." si el operador difiere de los aceptados.
#TODO: "Error: Numbers must only contain digits." si los operandos no son digitos numericos.
#TODO: "Error: Numbers cannot be more than four digits." si algun operando tiene mas de 4 digitos

#Condiciones
#TODO: El operador tendra una separacion de un espacio con referencia al operando mas largo y estara en la misma linea del segundo operando
#TODO: Los numeros estaran alineados a la derecha
#TODO: Cuatro espacios entre problema
#TODO: Guiones al final del bloque del problema, y cubriran todo el bloque, incluyendo el operador 


#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])


#Metodo que devuelve el tamaño maximo del bloque
def tamaño(bloque):
    bigger=0
    if len(bloque[0])>=len(bloque[2]):
        bigger=len(bloque[0])
    else:
        bigger=len(bloque[2])
    return bigger


##########Main
operaciones=["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


##########
for op in operaciones:
    print('operacion:',op)
    #en cada iteracion se tiene una operacion en forma de cadena de texto
    ops=op.split()
    x=tamaño(ops)


