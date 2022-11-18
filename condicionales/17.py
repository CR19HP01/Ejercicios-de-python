import os 
os.system("cls")

producto = int( input("Cuantas docenas compro : " ) )

PRECIO = 10

descuento = (0.15 if producto >= 6 else 0.10) * PRECIO * producto  

obsequio = ( 2 if producto / 3 and producto >= 30 else 0 ) * ( producto // 3 ) 

print( f'Monto de la compra : S/ { producto * PRECIO }')
print( f'Descuento          : S/ { descuento}' )
print( f'Total a pagar      : S/ { (PRECIO * producto) - descuento }')
print( f'Cantidad de obsequios: { obsequio } lapiceros' )
