def pedirData():
    nombre=""
    apellido=""
    carrera=""
    nombre=input("Introduce tu nombre:")
    apellido=input("Introduce tu apellido:")
    carrera=input("Introduce tu escolaridad:")
    datos=[nombre, apellido, carrera]
    return datos


print("Datos generales")
print(pedirData())








