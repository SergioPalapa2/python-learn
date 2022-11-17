#Datos en la web
# Protocolo request/response como base para el intercambio de datos
# Intercambio de datos entre plataformas
# Existen dos formatos usados habitualmente: XML JSON

#"wire protocol", lo que se envia al medio fisico (cableado)

# Serializacion: tomar informacion en un formato propio del lenguaje
# Deserializacion: Tomar informacion y prepararla al formato deseado
# ej: diccionario python ---> XML

# ej: JSON
# {
#     "name": "Serch"
#     "phone": 55664488
# }

#Formato XML (extensible markup languaje)
# El objetivo principal es ayudar a sistemas de informacion compartir datos estructurados
# diseñado para ser humanamente legible

# tags: indican el inicio o fin de los elementos
# atributos: pares key/value en la apertura de un tag XML 
# seriazar/deserializar: Conversion de los datos almacenable o transportable por los sistemas

# ej:
# <person> //tag inicio
#     <name>Serch</name>           
#     <phone type="intl"> //atributo
#         556699887 //contenido
#     </phone>
#     <email hide="yes"/>
# </person> //tag cierre

# Un elemento complejo incluye un tag que contiene mas tags
# arboles
# paths


#####XML schema
# Descripcion del formato legal de un doxumento XML
# Se expresa en terminos de restricciones en la estructura y contenido
# Regularmente usado para especificarse como un "contrato" entre sistemas.


# Especificacion w3c: XSD (.xsd)
# - xs: element
# - xs: sequence
# - xs: complexType

# <xs:complexType name="person">
#     <xs:sequence>
#         <xs:element name="lastname" type="xs:string"/>
#         <xs:element name="age" type="xs:integer"/>
#         <xs:element name="dateborn" type="xs:date"/>
#     </xs:sequence>
# </xs:complexType>

#XSD constraints
# <xs:complexType name="person">
#     <xs:sequence>
#         <xs:element name="lastname" type="xs:string"/>
#         <xs:element name="age" type="xs:integer"/>
#         <xs:element name="dateborn" type="xs:date"/>
#     </xs:sequence>
# </xs:complexType>

# <person>
#     <lastname>Severance</lastname>
#     <age>17</age>
#     <dateborn>2001-04-17</dateborn>
# </person>


####################
#XSD constrains#
# <xs: element name="person">
#     <xs:complexType>
#         <xs:sequence>
#             <xs:element="full_name" type="xs:string"
#                 minOccurs="1" maxOccurs="1"/>
#             <xs:element="child_name" type="xs:string"
#                 minOccurs="0" maxOccurs="10"/>
#         </xs:sequence>
#     </xs:complexType>
# </xs: element >


# <person>
#     <full_name>Tove Refsnes</full_name>
#     <child_name>Hege</child_name>
#     <child_name>Stale</child_name>
#     <child_name>Jim</child_name>
#     <child_name>Borge</child_name>
# </person>


#######################
#XSD Data types
# <xs:element name="customer" type="xs:string"/>
# <xs:element name="start" type="xs:date"/>
# <xs:element name="startdate" type="xs:dateTime"/>
# <xs:element name="prize" type="xs:decimal"/>
# <xs:element name="weeks" type="xs:integer"/>

# <customer>John Smith</customer>
# <start>2002-09-24</start>
# <startdate>2002-05-30T09:3010Z</startdate>
# <prize>999.5<prize/>
# <weeks>30</weeks>
#Es comun representar horario en formato UTC/GMT
#dado el como se usa en servers alrededor del mundo

#ISO 8601 Formato fecha-hora
#year-month-day T[time off day] Z(Zona, generalmente especificada en UTC/GMT)

#Manejo de XML en python
import xml.etree.ElementTree as ET

data='''<person>
     <name>chuck</name>
     <phone type="inil">
         7343034456
     </phone>
     <email hide="yes"/>
</person>'''

tree=ET.fromstring(data) #objeto del cual se puden hacer consultar y sacar informacion
print("Name:", tree.find('name').text) #texto
print("Attr:", tree.find('email').get('hide')) #atributo


input='''<stuff>
    <users>
        <user x='2'>
            <id>001</id>
            <name>chuck</name>
        </user>
        <user x='7'>
            <id>009</id>
            <name>trent</name>
        </user>
    </users>
</stuff>'''

stuff=ET.fromstring(input)
primero=stuff.findall('users/user')
print('User count:', len(primero))
for item in primero:
    print('Name:',item.find('name').text)
    print('ID:',item.find('id').text)
    print('Atrib:',item.get('x'))


