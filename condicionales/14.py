import random
import os
os.system("cls")

ntarjeta = random.randint(1,999)
importe = int( input("Importe : "))

if ntarjeta % 2 == 0 and  ntarjeta >= 100 : descuento =  importe * 0.15 
else : descuento =  importe * 0.05 

print( f'Número de la tarjeta : {ntarjeta}' )
print( f'Descuento            : S/ {descuento}' )
print( f'Total                : S/ {importe - descuento }' )
