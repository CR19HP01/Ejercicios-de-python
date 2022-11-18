import os
os.system("cls") 

total = int( input( "Ingrese la donación anual : " ) )

centroSalud = total * 25 / 100
comedorInfantil = total * 35 / 100
escuelaInfantil = total * 25 / 100
asilo = total * 15 / 100

#montos
print( f'Repartición de donación:\n Centro de salud : {centroSalud} \n Comedor Infantil : {comedorInfantil} \n Escuela Infantil : {escuelaInfantil} \n Asilo de ancianos : {asilo} ' )
