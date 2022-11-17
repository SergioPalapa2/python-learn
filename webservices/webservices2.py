#Javascript Object Notation
#JSON

#Ideal para buscar y sacar informacion que se compartira entre sistemas
#JSON representa datos como listas y/o diccionarios anidados

import json  #importante en minusculas
data='''{
    "name":"chuck",
    "phone":{
        "type":"intl",
        "number":"+52 4499887722"
    },
    "email":{
        "hide":"yes"
    }
}'''


data2='''["calculo","geometria","fisica","quimica organica"]''' #importante usar ""


info=json.loads(data)
print('Name:',info['name'])
print('Hide:',info['email']['hide'])


info2=json.loads(data2)
print("Materia:",info2[0])
print("Materia:",info2[1])
print("Materia:",info2[2])
print("Materia:",info2[3])


#Arreglo de diccionarios
filej='''[
    {
        "id":123,
        "x":"2",
        "name":"Serch"
    },
    {
        "id":124,
        "x":"6",
        "name":"Nan"
    }
]'''
exp=json.loads(filej)
print("Usuarios: ", len(exp))
for item in exp:
    print("Nombre",item["name"])
    print("ID",item["id"])
    print("Atrib",item["x"])
