import os
os.system("cls")

numero = int( input("Ingresar número de cuatro cifras : ") ) 

estadoCivil = ( numero % 10000 - numero % 1000 ) // 1000

if estadoCivil == 1 : estado = "Soltero"
if estadoCivil == 2 : estado = "Casado"
if estadoCivil == 3 : estado = "Viudo"
if estadoCivil == 4 : estado = "Divorciado"

edad = ( numero % 1000 - numero % 10 ) // 10

sexo = numero % 10

if sexo == 1 : sexo1 = "Femenino" 
if sexo == 2 : sexo1 = "Masculino"

print (f'Estado Civil : {estado}')
print (f'Edad         : {edad} años')
print (f'Sexo         : {sexo1}')
print ()