import os
os.system("cls")

cont = 0

for x in range(100,999) :
    if x % 10 ==( x % 1000 - x % 100 ) // 100:
        cont += 1

print(f'Total de números de 3 cifras que son capicua : {cont}')
