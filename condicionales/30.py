import os
os.system("cls")

cuota = float(input ('Valor de cuota : '))
dia = int(input ('Día de pago : '))

descuento, recargo = 0, 0

if dia <= 10:
    descuento = cuota * 0.02

if dia <= 10 and descuento < 5:
    descuento = 5

if dia > 20:
    recargo = cuota * 0.03

if dia > 20 and recargo < 10:
    recargo = 10

print ('Valor de descuento             : S/', descuento)
print ('Valor de recargo               : S/', recargo )
print ('Valor de importe total a pagar : S/', cuota - descuento + recargo)
print ()