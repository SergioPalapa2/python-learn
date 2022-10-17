#Identificar letras error en una cadena
#Aceptable de a a m
#Cualquiera otra es error
#La funcion devolvera el error encontrado en la cadena

def error(cadena):
    c=0
    for char in cadena:
        if char=="n" or char=="o" or char=="p" or char=="q" or char=="r" or char=="s" or char=="t" or char=="u" or char=="v" or char=="w" or char=="x" or char=="y" or char=="z":
            c=c+1  
    return str(c)+"/"+str(len(cadena))
    


cad="aaabbbpppzaaaq"
print(error(cad))

