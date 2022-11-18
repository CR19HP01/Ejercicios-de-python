import os
os.system("cls")

base= int(input("Base : " ) ) 
exponente = int(input( "Exponente : " ) )

resultado = 1
#res = base ** exponente

for i in range(exponente) :
    resultado *= base

print(f'Respuesta : {resultado}')