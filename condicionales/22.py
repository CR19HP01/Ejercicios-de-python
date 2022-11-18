import os
os.system("cls")

productoA = int( input( "Cantidad de unidades del producto A : " ) ) 
productoB = int( input( "Cantidad de unidades del producto B : " ) ) 

precioA = 25
importeA = precioA * productoA
descuento = (0.15 if productoA > 50 else 0) * importeA

precioB = 30
importeB = precioB * productoB
descuentoB = (0.1 if productoB > 60 else 0) * importeB

print()
print(f'Importe bruto del producto A seria {importeA} mas producto B seria {importeB}: S/. { importeA + importeB }')
print()
print(f'Descuento del producto A seria {descuento} mas producto B seria {descuentoB} : S/. { descuento + descuentoB }')
print()
print(f'Total a pagar       : { (importeA - descuento) + (importeB - descuentoB) }')