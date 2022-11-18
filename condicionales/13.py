import os
os.system("cls")

numero = int( input("Número de tres cifras : " ) )

if numero >= 100 and numero <= 999 : 
    a = numero /100
    b = numero % 100 / 10
    c = numero % 100 % 10 

if a == b + 1 and b == c + 1 or c == b - 1 and b == a - 1 :
    print( "Consecutivo" )
elif a < b < c : print("Ascendente")
elif a > b > c : print("Descendente")
else : print( "No consecutivo" )


