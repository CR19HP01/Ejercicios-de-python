import os
os.system("cls")

categoria = input("Categoría : ")

pagoHora = 0

if categoria == "A" or categoria == "a": pagoHora = 21 
if categoria == "B" or categoria == "b": pagoHora = 19.5
if categoria == "C" or categoria == "c": pagoHora = 17
if categoria == "D" or categoria == "d": pagoHora = 15.5

horaTotal = 128

sueldoBruto = horaTotal * pagoHora
if sueldoBruto > 2500 : descuento  = 0.2 * sueldoBruto 
else : descuento = 0.15 * sueldoBruto

print(f'Sueldo Bruto : {sueldoBruto}')
print(f'Descuento : {descuento}')
print(f'Sueldo Neto : {sueldoBruto - descuento}')
