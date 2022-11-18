import os
os.system("cls")

montoTotal = int( input("Monto total vendido : " ) ) 

if montoTotal > 5000 :
    sueldo = montoTotal * 0.1 + 25 *(montoTotal / 500)
else : sueldo = 0.1 * montoTotal

print("Sueldo : S/. ",sueldo)