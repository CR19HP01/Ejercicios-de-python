import os
os.system("cls")

PI = 3.14
radio = int( input( "Radio: " ) )
altura = int( input( "Altura: " ) )

area = 2 * PI * radio * ( radio + altura )
volumen = PI * radio**2 * altura

print( f'Área: { area } unidad²' )
print( f'volumen: { volumen } unidad³' )
