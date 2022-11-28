#Procesar cadenas donde # representa un backspace
#funcion chr() retorna el caracter representado por la cifra en asscii
#funcion ord() retorna el numero que representa el caracter

#text='acb##dert#sxsx####'
text="D##2C[7#"

textl=list(text)
c=0
textf=list()
for char in textl:
    if char!="#":
        textf.append(char)
    else:
        if textf==[]:
            pass 
        else: textf.pop()

textf="".join(textf)

print(textf)