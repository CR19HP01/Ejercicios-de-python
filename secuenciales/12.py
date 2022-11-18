import math
import os
os.system("cls")

a = int( input("Ingrese variable 'a' : ") )
b = int( input("Ingrese variable 'b' : ") )
c = int( input("Ingrese variable 'c' : ") ) 

discriminante = ( (b**2) + (-1 * 4 * a * c) ) ** 1/2
x1 = ( (-1 * b) + discriminante ) / 2 * a
x2 = ( (-1 * b) - discriminante ) / 2 * a

print( f'Soluciones : ' )
print( f'Solución {x1} y {x2}')
 
