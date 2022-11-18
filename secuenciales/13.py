import os
os.system("cls")

cOpuesto = int( input(" Ingrese cateto opuesto : ") )
cAdyacente = int( input(" Ingrese cateto adyacente : ") )
hipotenusa = (cOpuesto**2 + cAdyacente**2) ** 0.5

print( f'Hipotenusa : {hipotenusa:.2f}' )

