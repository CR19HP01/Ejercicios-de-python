import os
os.system("cls")

#numero = int( input("Número de 4 cifras : ") )

#dig1 = numero // 1000
#dig2 = ( numero - dig1 * 1000) // 100
#dig3 = ( numero - dig1 * 1000 - dig2 * 100 ) // 10
#dig4 = ( numero - dig1 * 1000 - dig2 *100 - dig3 * 10 ) // 1

#if numero < 10000 and numero > 999 : 
#    if dig1 % 2 == 0 and dig2 % 2 == 0

cont = 0

for x in range(1000, 9999) :
    dig1 = x // 1000
    dig2 = ( x - dig1 * 1000) // 100
    dig3 = ( x - dig1 * 1000 - dig2 * 100 ) // 10
    dig4 = ( x - dig1 * 1000 - dig2 *100 - dig3 * 10 ) // 1

    sumaPar = 1
    sumaImpar = 1
    
    if sumaPar == sumaImpar :

        if dig1 % 2 == 0 and dig2 % 2 == 0 and dig3 % 2 == 0 and dig4 % 2== 0 :  
            sumaPar = dig1 + dig2 + dig3 + dig4
        elif dig1 %2 != 0 and dig2 %2 != 0 and dig3 %2 != 0 and dig4 %2 != 0 : 
            sumaImpar = dig1 + dig2 + dig3 + dig4

            cont += 1
    x += 1

print(f'Condición : La suma de las cifras pares e igual a la suma de las cifras impares')
print(f'Cantidad de números de 4 cifras que cumplen la condición : {cont}')
print()