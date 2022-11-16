import re

def encrypt_this(text):
    newtxt=text.split()
    for word in newtxt:
        new=str(ord(word[0]))
        print(re.search('^Nombre',line))
        print(new)

print(encrypt_this("Hola mundo"))
