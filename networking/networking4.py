#Libreria urllib
#Al ser HTTP un protocolo muy común, python provee una libreria que hace mas facil el manejo de sockets
#Hace que podamos procesar paginas web como archivos
import urllib.request
import urllib.parse
import urllib.error


fhand=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip() )


#Como archivo
counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)


#Lectura de paginas web
whand=urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
for line in whand:
    print(line.decode().strip())




