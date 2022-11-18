import os
os.system("cls")

montoVendido = int( input("Monto vendido : ") )

sBasico = 250
comision = 0.05 if montoVendido < 5000 else 0.15 if montoVendido >20000 else 0.08 if 5000 < montoVendido < 10000 else 0.10

sBruto = sBasico + comision

#descuento = 0
#if sBruto > 3500 : descuento = 0.15 * sBruto
#else : descuento = 0.08 * sBruto

descuento = (0.15 if sBruto > 3500 else 0.08) * sBruto

print( f'Sueldo Bruto : S/ { sBruto } ' )
print( f'Descuento    : S/ { descuento }' )
print( f'Comisión     : S/ { comision }' )
print( f'Sueldo Neto  : S/ { sBruto - descuento }' )

#falta comprobar

