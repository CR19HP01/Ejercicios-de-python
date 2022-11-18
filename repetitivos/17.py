import os
os.system("cls")

def indexOf(valor) :
    contenedor = 0
    for x in range(len(palabra)) :
        contenedor += 1

        for i in range (len(valor)):
            if palabra[x] == valor[i] :
                print(f'Índice es : {x}')
                contenedor -= 1
                break

    if contenedor == len(palabra) :
        print(f'No hay valor : ')
            
palabra = input ("Palabra : ")
v = indexOf(input("Valor buscado : "))
print()