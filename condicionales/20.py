import os
os.system("cls")

n1 = int( input( "Número 1 : " ) )
n2 = int( input( "Número 2 : " ) )
n3 = int( input( "Número 3 : " ) )

if n1 >= n2 and n1 >= n3 and n2 >= n3 : print("Orden : Ascendente")
elif n1 <= n2 and n1 <= n3 and n2 <= n3 : print("Orden : Descendente")
else : print("Orden : Desordenado")