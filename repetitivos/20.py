import os
os.system("cls")

mayor, menor, cont = 0, 100000, 0

for i in range(1, 11) :
    n = int( input("Promedio "+str(i)+" : ") )
    mayor = n if n > mayor else mayor
    menor = n if n < menor else menor
    cont += n

print(f'Menor promedio : {menor}')
print(f'Mayor promedio : {mayor}')
