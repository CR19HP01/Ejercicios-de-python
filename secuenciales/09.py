import os
os.system("cls")

numero = int(input( "Ingrese numero: " ))
c1 = numero // 1000
c2 = (numero % 1000) // 100
c3 = ((numero % 1000) % 100) // 10
c4= numero % 10

print( f'La suma de cifras : {c1+c2+c3+c4}' )