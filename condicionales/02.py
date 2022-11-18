import os
os.system("cls")

unidad = int( input( "Unidades : " ) ) 

caramelo = 5 if unidad <= 50 else 15 if unidad >= 100 else 10

precio = 20
compra = precio * unidad

#descuento = 0.14 * compra
#if compra <= 500 : descuento = 0.12 * compra
#elif compra > 700 : descuento = 0.16 * compra
descuento = (0.12 if compra <= 500 else 0.16 if compra > 700 else 0.14 ) * compra

print( "Compra : S/ ",compra)
print( "Número de caramelo : ",caramelo )
print( "Descuento : S/ ",descuento)
print( "Total : S/ ",compra - descuento)