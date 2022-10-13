#instalar pandas (pip install pandas)
#instalar xlrd (pip install xlrd)
#instalar openpyxl (pip install openpyxl)
import pandas as pd

archivo=pd.read_excel('Registros.xlsx') #lectura de archivo
print(archivo)

dicc=archivo.to_dict() #metodo de pands para convertir en un diccionario
print(dicc)

jsonfile=archivo.to_json()
print(jsonfile)