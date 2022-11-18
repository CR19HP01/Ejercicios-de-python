import os
os.system("cls")

n = int( input("Número : " ) )

nprimos = 0
i = 1

while i <= n:
    for x in range( 2, n//2 + 1) :
        if n % x == 0 : break
    
    else :
        nprimos += 1 
    i += 1        


if nprimos != 0 : 
    print(nprimos, "es primo")
else: print("No es primo")