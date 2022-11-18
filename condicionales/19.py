import os
os.system("cls")

edad = int( input( "Edad : " ) )
sexo = input( "Sexo : " ) 

if edad <= 23 and sexo == "femenino" : print("Categoría : FA")
elif sexo == "femenino" : print("Categoría : FB") 

if edad <= 25 and sexo == "masculino" : print("Categoría : MA")
elif sexo == "masculino" : print("Categoría : MB")

