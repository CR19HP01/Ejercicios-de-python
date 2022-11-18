import os
os.system("cls")

promedio = float( input("Promedio Ponderado : " ) )
categoria = input("Categoria : ")

pension = 0

if promedio <= 20 : 
    if categoria == "A" : pension = 550 
    if categoria == "B" : pension = 500
    if categoria == "C" : pension = 450
    if categoria == "D" : pension = 400

descuento = (0 if promedio <= 13.99 else 0.15 if 18 <= promedio <= 20 else 0.1 if 14 <= promedio <= 15.99 else 0.12) * pension    

print(f'Pensión actual : {pension}')
print(f'Descuento : {descuento}')
print(f'Nueva pensión : {pension - descuento}')
