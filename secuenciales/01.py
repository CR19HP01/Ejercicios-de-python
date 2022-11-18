import os
os.system("cls")

#Entrada
varones = int ( input ( "Ingrese el numero varones : " ) )
mujeres = int ( input ( "Ingrese el numero mujeres : " ) )
total  =  varones + mujeres 

#Proceso
p_varon = varones * 100 / total
p_mujer = mujeres * 100 / total

#Salida
print()
print ( f'Resultado de las varones : {p_varon} %')
print ( f'Resultado de las mujeres : {p_mujer} %')
