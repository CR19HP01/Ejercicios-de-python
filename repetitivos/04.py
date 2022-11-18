import os
os.system("cls")

n = int( input("Número : " ) )
m = int( input ("Cantidad de multiplos : " ) )

for x in range(n, (n*m) + 1, n) :
    print(x, " ",end=" ")