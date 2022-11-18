import os 
os.system("cls")

donacion = int( input( "Donación : " ) )

if donacion >= 10000:
    centroSalud = donacion * 0.03
    comedor = donacion * 0.05
    bolsa = donacion * 0.02
elif donacion < 10000 :
    centroSalud = donacion * 0.25
    comedor = donacion * 0.06
    bolsa = donacion * 0.15

print( f'Centro de Salud  : S/ {centroSalud}' )
print( f'Comedor de niños : S/ {comedor}' )
print( f'Bolsa            : S/ {bolsa}' )