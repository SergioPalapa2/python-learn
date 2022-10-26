#Regresa el numero de 1s encontrados en la representacion binaria de un numero de entrada
def count_bits(n):
    b=bin(n) #convert dec to bin
    count=0
    for bit in b:
        if bit=='1':
            count=count+1
        else: pass
    return count


print(count_bits(1234))


#Solucion alternas
# def countBits(n):
#     return bin(n).count("1")


