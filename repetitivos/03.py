import os
os.system("cls")

n = int( input( "Número : " ) )

cont = 0
for div in range (1, n+1) :
    if n % div == 0 :
        cont += 1
print(f'El número {n} tiene {cont} divisores')