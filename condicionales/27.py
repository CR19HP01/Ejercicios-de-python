import os
os.system("cls")

montoVendido = int( input("Monto vendido : " ) ) 

sueldoBasico = 600

comision = montoVendido* 0.15
sueldoBruto = sueldoBasico + comision

if sueldoBruto > 1800 : descuento = 0.1 *sueldoBruto
else : descuento = 0.05 * sueldoBruto

obsequio = 3 if montoVendido > 1000 else 1

print(f'Sueldo Bruto  : S/. {sueldoBruto}')
print(f'Descuento     : S/.{descuento}')
print(f'Sueldo neto   : S/. {sueldoBruto - descuento}')
print(f'Obsequio      : {obsequio} polos')