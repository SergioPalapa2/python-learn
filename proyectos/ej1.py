#Funcion que recibe una lista de cadenas que representan problemas aritmeticos.
#Regresa las operaciones acomodadas de forma vertical, una a lado de otra.
#Toma un segunda argumento, si es "true" se mostrara el resultado.


#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

prueba=["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(lista):
    return


for op in prueba:
    #en cada iteracion se tiene una operacion en forma de cadena de texto
    ops=op.split()
    bigger=0
    if len(ops[0])>=len(ops[2]):
        bigger=len(ops[0])
    else:
        bigger=len(ops[2])

    print(bigger)



    









