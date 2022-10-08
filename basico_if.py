print("Calculando pago")

#funcion que calcula el pago
def computepay(horas, sueldohr):
    if(horas>40): #funcion que condiciona la ejecucion de bloques de codigo
        reg=horas*sueldohr
        otp=(horas-40)*(sueldohr*0.5)
        total=reg+otp
    else:
        total=horas*sueldohr

    print("Calculo terminado")
    return total

sal=float(input("Salario por hora: "))
hr=float(input("Horas laboradas: "))


#llamada a la funcion
pago=computepay(hr,sal)

print("Total a pagar: ", pago)



