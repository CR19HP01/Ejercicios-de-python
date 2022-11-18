import os 
os.system("cls")

unidades = int ( input( "Unidades : " ) )

#precio = 0
#if unidades <= 25 : precio = 27
#elif unidades >=2 26 and unidades <= 50 : precio = 25
#else : precio = 23

#precio = 25
#if unidades <= 25 : precio = 27
#elif unidades >= 51 : precio = 23

precio = 27 if unidades <=25 else 23 if unidades >= 51 else 25
compra = unidades * precio

#descuento = 0.05 * compra
#if unidades >= 50 : descuento = 0.15 * compra

descuento = ( 0.15 if unidades >= 50 else 0.05 ) * compra

print( f'Precio    : S/ {precio:.2f}' )
print( f'Compra    : S/ {compra:.2f}' )
print( f'Descuento : S/ {descuento:.2f}' )
print( f'Total     : S/ {compra-descuento:.2f}' )

