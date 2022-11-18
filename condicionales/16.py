import os
os.system("cls")

ingresoComprador = int( input( "Ingreso mensual del comprador : " ) )

casa = 4500

if ingresoComprador < 1250 : cuota = casa * 0.15 ; cuotaMensual = (casa - cuota) / 120
elif ingresoComprador >= 1250 : cuota = casa * 0.3 ; cuotaMensual = (casa - cuota ) / 75

print(f'Cuota Inicial : S/. {cuota}')
print(f'Cuota Mensual : S/. {cuotaMensual}')