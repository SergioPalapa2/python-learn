#contar cada caracteres en un string

def count(string):
    counts=dict()
    if string=="":
        return {}
    else:
        for char in string:
            counts[char]=counts.get(char,0)+1
        return counts

print(count(""))



# #Soluciones alternas
# def count(string):
#     return {i: string.count(i) for i in string}


  

