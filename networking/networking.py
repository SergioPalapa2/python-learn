#Networking

#TCP
#Trabaja en la parte mas arriba de ip(internet protocol)
#Se maneja el control del flujo de datos usando una ventana de transmisoin
#Provee una especie de "pipe"


#Sockets

# Los websockets comunican procesos bidireccionales en una red o en internet
# process<-------(nternet)---------->process

# Puertos
# Punto especifico de conexion que utiliza una aplicacion
# Permite la interaccion de mltiples procesos o conexiones a un msmo server

# -telnet: 23
# -ssh: 22
# -http: 80
# -https: 443
# -smtp: 25
# -imap: 143/220/993
# -pop: 109/110
# -dns: 53
# -ftp: 21 


#Sockets en python
import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))




