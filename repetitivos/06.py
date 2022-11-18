import os
os.system("cls")

n = int( input( "Número : " ) )

cont = 0

for a in range(1,13) : 
    print( f'{n} x {a} = {(n * a)}' )
#    cont += 16