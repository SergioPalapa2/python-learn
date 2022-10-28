#Realizar una "mexican wave" con los caracteres que entran a la funcion


def wave(people):
    lst=list()
    waver=list()
    c=0
    for letter in people: #Create a list with all chars
        lst.append(letter)
    
    for char in lst: #Capitalize letter and create a item in a new list
        if lst[c]==' ':
            c=c+1
            pass
        else:
            lst[c]=char.upper()
            temp=''.join(lst)
            waver.append(temp)
            lst[c]=char.lower()
            c=c+1
    return waver



# print(wave('holita mama'))

# Soluciones alternas
# def wave(str):
#     return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]







