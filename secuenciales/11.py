import os
os.system("cls")

numero1 = input("Ingrese número de 3 cifras : ")
numero2 = input("Ingrese número de 3 cifras : ")

#Para el cambio de posicion de la cifra tiene que tomarlo  como  caracter
nNumero1 = numero2[2] + numero1[1] + numero2[0]
nNumero2 = numero1[2] + numero2[1] + numero1[0]

print()
print( f'Cambio de posición de los cifras : ')
print( f'Número 1 : {nNumero1}')
print( f'Número 2 : {nNumero2}')
