#Generador de hashtags
#Generar un hashtag con un strind de entrada
#Se tienen que mostrar las palabras juntas y cada una con su inicial mayuscula

def generate_hashtag(s):

    s1=s.split()
    hashtag=""

    for word in s1:
        hashtag=hashtag+word.capitalize()


    if hashtag=="" or len(hashtag)>140:
        return False
    else:
        hashtag="#"+hashtag
        return hashtag



cadena="saddassasa  sdss sdssd sds sdsds  sdsds sdsdsd asdsadsadsads sadsadsadsad asdsadsadsadsa dsadsadsadsad sadsadsadsad sadsadsadsad asdsadsadsa "
print(len(cadena))
print(generate_hashtag(cadena))



#soluciones alternas
# def generate_hashtag(s):
#     output = "#"
    
#     for word in s.split():
#         output += word.capitalize()
#     return False if (len(s) == 0 or len(output) > 140) else output



# def generate_hashtag(s):
#     ans = '#'+ str(s.title().replace(' ',''))
#     return s and not len(ans)>140 and ans or False
    

