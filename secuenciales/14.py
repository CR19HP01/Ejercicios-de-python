import os
os.system("cls")

numero1 = int( input( "Ingrese numero  1 : "))
numero2 = int( input( "Ingrese numero  2 : "))
numero3 = int( input( "Ingrese numero  3 : "))
numero4 = int( input( "Ingrese numero  4 : "))
numero5 = int( input( "Ingrese numero  5 : "))

lista = list( (numero1, numero2, numero3, numero4, numero5) )
lista.sort() #ordenar la lista en ascendente
promedio = ( numero1 + numero2 + numero3 + numero4 + numero5 - lista[0] -lista[1] )

print( f'Promedio : {promedio:.2f}' )
print( f'Número máximo : {lista[4]}' ) #El primer numero maximo
print( f'Número mínimo : {lista[0]}' ) #El primer numero minimo
print()


