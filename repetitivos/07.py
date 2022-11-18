
def factorial(numero):
    if numero <= 0: 
        return 1
    factorial = 1
    while  numero != 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

valor = int( input("Número : "))
f = factorial(valor)
print(f'Factorial de {valor} es {f}')