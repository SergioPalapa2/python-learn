#Devuelve una cadena con las palabras salteadas al reves

def reverse_alternate(s):
    words=s.split()
    for x in range(1,len(words),2):
        words[x]=words[x][::-1]
    s2= " ".join(words)
    return s2







    


