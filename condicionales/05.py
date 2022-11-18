import os
os.system("cls")

numero = int( input( "Número : " ) )

dig1 = numero // 1000
dig2 = ( numero - dig1 * 1000) // 100
dig3 = ( numero - dig1 * 1000 - dig2 * 100 ) // 10
dig4 = ( numero - dig1 * 1000 - dig2 *100 - dig3 * 10 ) // 1

lista = [dig1, dig2, dig3, dig4]
lista.sort()

sumaMax = str(lista[3]) + str(lista[0])
print("Mayor número posible :",sumaMax)
