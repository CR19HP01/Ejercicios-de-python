import os
os.system("cls")

cuaderno = int( input("Cantidad de cuadernos : " ) )

#Reglas de redondeo
#Si el decimal 5 sigue a una cifra impar, la redondea al alza. Ejemplo: 73,5 se redondea a 74.
#Si el decimal 5 sigue a una cifra par, la redondea a la baja. Ejemplo: 78,5 se redondea a 78.

if cuaderno % 2 == 0 : cada = cuaderno // 4
else : cada = (cuaderno // 4) + 1 

if cuaderno % 2 == 0 : cada1 = cuaderno // 6
else : cada1 = (cuaderno // 6) + 1

if cuaderno % 2 == 0 : cada2 = cuaderno // 12
else : cada2 = (cuaderno // 12) + 1

obsequio = 0 if cuaderno < 12 else 1 * cada if 12 <= cuaderno < 24 else 2 * cada if 36 > cuaderno >= 24 else (2 * cada) + (1 * cada1) + 1 * cada2 if cuaderno >= 36 else 0

print(f'Cantidad Obsequiada : {obsequio} lapiceros')