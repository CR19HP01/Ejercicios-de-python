import os
os.system("cls")

nMes = int( input( "Valor numérico del mes : " ) )
año = int( input( "Año : " ) )

listaMes = list(("Enero", "Febrero","Marzo", "Abril", "Mayo","Junio", "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre"))

M =listaMes[nMes - 1]

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0) and M =="Febrero" : print("  ** Es bisiesto **  ") ; diaMes = 29
elif M == "Febrero" : diaMes = 28
elif M == "Abril" or M == "Junio" or M =="Setiembre" or M =="Noviembre" : diaMes = 30
elif M == "Enero"or M =="Marzo" or M =="Mayo" or M =="Julio"or M =="Agosto" or M =="Octubre" or M =="Diciembre" : diaMes = 31

print(f'Mes : {M}')
print(f'{M} tienes { diaMes } dias')