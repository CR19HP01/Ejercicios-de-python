import os
os.system("cls")

montoTotal = float( input("Monto total de la compra : S/. ") )

if montoTotal > 5000 : banco = 0.3 * montoTotal
else : banco = 0.2 * montoTotal

diferencia = montoTotal - banco
prestamo = banco * 0.1 + banco

print(f'Cantidad que la empresa tiene que pagar : S/. {diferencia}')
print(f'Prestamo del banco                      : S/. {prestamo}')