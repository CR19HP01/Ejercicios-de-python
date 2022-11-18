import os 
os.system("cls")

n = int(input("Número : ") )

cont = 0

for x in range(n+1) :
    if x%3 == 0 and not x%5 == 0 :
        cont += x

print(f'Suma de multiplos : {cont}')