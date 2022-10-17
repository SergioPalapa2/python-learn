#Suma de los dos numeros menores en un arreglo

def likes(names):
    # your code here
    c=0

    if len(names)==0:
        return "no one likes this"

    elif len(names)==1:
        return names[0]+" likes this"
        
    elif len(names)==2:
        return names[0]+" and "+names[1]+" like this"
        
    elif len(names)==3:
        return names[0]+", "+names[1]+" and "+names[2]+" like this"

    elif len(names)>3:
        for count in names:
            c=c+1
        return names[0]+", "+names[1]+" and "+c-2+"others like this" #no es posible concatenar un int con strings (convertir a str)
    pass





nom=["a","b","c","d"]
# nom=["a","b","c","d","e"]
print(likes(nom))
