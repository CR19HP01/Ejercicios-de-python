import os
os.system("cls")

multi = int( input("Multiplicando : ") )
multiplicador = int( input("Multiplicador : ") )

producto = 0
for a in range( multiplicador ) :
    producto += multi
print( f'Producto : {producto}' )

#producto = 0
#while multiplicador > 0 :
#    producto += multi
#    multiplicador -= 1 
#print( f'Producto : {producto}' )