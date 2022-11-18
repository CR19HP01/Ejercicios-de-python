import os
os.system("cls")

def inverTex(cadena):
    cadenaInver= ""
    for letra in cadena:
        cadenaInver = letra + cadenaInver
    return cadenaInver

valor = input("Texto : ")
f = inverTex(valor)

print("Texto ",valor, "invertido seria ",f)