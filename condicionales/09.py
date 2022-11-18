import os
os.system("cls")

unidad = int( input( "Unidades : " ) )
codigo = int( input("Código    : " ) )


if codigo == 101 : precioUnitario = 17 
if codigo == 102 : precioUnitario = 25
if codigo == 103 : precioUnitario = 16
if codigo == 104 : precioUnitario = 27

descuento = (0.05 if unidad <= 10 else 0.13 if unidad >= 31 else 0.08 if 11 <= unidad <= 20 else 0.10) * precioUnitario  

print(f'Importe de la compra  : S/. {unidad * precioUnitario}')
print(f'Descuento             : S/. {descuento}')
print(f'Total                 : S/. {unidad * precioUnitario - descuento}')