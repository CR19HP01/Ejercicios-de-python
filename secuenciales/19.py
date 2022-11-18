import os
os.system("cls")

montoVendido = int( input( "Cantidad total vendida : " ) )
sueldoBasico = 500

comision = montoVendido * 0.09
sueldoBruto = sueldoBasico + comision 
descuento = sueldoBruto * 0.11
sueldoNeto = sueldoBruto - descuento

print( f'Comisión : {comision}\nSueldo bruto : {sueldoBruto}\nDescuento : {descuento}\nSueldo neto : {sueldoNeto}')
