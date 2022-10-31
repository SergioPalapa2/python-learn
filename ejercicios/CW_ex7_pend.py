#Regresar un numero en su forma expandida
#Ejemplo 132 => 100+30+2

def expanded_form(num):
    strn=str(num)
    lon=len(strn)
    arr=[]
    for n in strn: #Create array with expanded elements
        lon=lon-1
        element=str(n)
        for m in range(lon):
            element=element+'0'
        arr.append(element)
    final=""
    for l in arr: #Create final form
        final=final+l+"+"
    final=final[0:len(final)-1] #remove last +
    return final

print(expanded_form(0))