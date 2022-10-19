#Funcion que recibe un arreglo de 10 digitos, entre 0 y 9
#Regresa una cadena con los numeros en forma de numero telefonico
#ejemplo entrada=[1,2,3,5,7,9,6,4,8,3] => (123) 579-6483

def create_phone_number(n):
    numerot='('
    c=0
    for i in n[:3]:
        numerot=numerot+str(i)
    numerot=numerot+")"+" "
    for i in n[3:6]:
        numerot=numerot+str(i)
    numerot=numerot+"-"
    for i in n[6:10]:
        numerot=numerot+str(i)
    return numerot


numero=[2,5,6,5,9,3,1,7,9,6]
print(create_phone_number(numero))


#solucion alterna
# def create_phone_number(n):#solucion
    # n = "".join([str(x) for x in n] )#solucion
    # return("(" + str(n[0:3]) + ")" + " " + str(n[3:6]) + "-" + str(n[6:]))