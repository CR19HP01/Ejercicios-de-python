import os 
os.system("cls")


n1 = int( input("Nota 1 : " ) )
n2 = int( input("Nota 2 : " ) ) 
n3 = int( input("Nota 3 : " ) ) 
n4 = int( input("Nota 4 : " ) ) 
n5 = int( input("Nota 5 : " ) )

if n1<=20 and n2<=20 and n3<=20 and n4<=20 and n5<=20 : eliminarMax = max(n1,n2,n3,n4,n5); eliminarMin = min(n1,n2,n3,n4,n5) 
else : print(f'Vuelve a ingresar las notas ') 
n1 = int( input("Nota 1 : " ) )
n2 = int( input("Nota 2 : " ) ) 
n3 = int( input("Nota 3 : " ) ) 
n4 = int( input("Nota 4 : " ) ) 
n5 = int( input("Nota 5 : " ) )
if n1<=20 and n2<=20 and n3<=20 and n4<=20 and n5<=20 : eliminarMax = max(n1,n2,n3,n4,n5); eliminarMin = min(n1,n2,n3,n4,n5) 

print(f'Mayor nota {eliminarMax} y menor nota {eliminarMin} eliminada')
print(f'Promedio : {(n1+n2+n3+n4+n5 - eliminarMax - eliminarMin) / 3}')
