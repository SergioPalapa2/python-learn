print("Pagos")

bruto=input("Salario por hora: ")
hours=input("Horas laboradas: ")

bruto1=float(bruto)
hours1=float(hours)

payment=(bruto1*hours1)-(bruto1*0.16)
print("Pago correspondiiente: ", payment)