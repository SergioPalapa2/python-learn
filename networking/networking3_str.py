#Sistema ASCII
#Cada caracter se representa por un numero entre 0 y 250, almacenados en 8 bits( 1 byte)
#ord() --> Devuelve el valor numerico de un caracter ASCII

print(ord("K"))
print(ord("L"))
print(ord("k"))
print(ord("l"))
print(ord("\n"))

#UTF-16 fixed-length 2 bytes
#UTF-32 fixed-length 4 bytes
#UTF-8 1-4 bytes
#Se recomienda UTF para codificar datos que seran intercambiados entre sistemas

#Nota: En python 3 todas las cadenas son UNICODE
x=u'abc' #//unicode
x2=b'abc'
print(x,x2)
print(type(x),type(x2))

#Al enviar datos a algun proceso externo (socket) enviamos bytes
#Es necesario codificar cadenas para ser enviadas
#cuando se lee desde un recurso externo es necesario decodificar

# while True:
#     data=mysock.recv(512)
#     if(len(data)<1):
#         break
#     mystring=data.decode()
    

#HTTP REQUEST EN PYTHON

