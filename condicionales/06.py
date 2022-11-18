import  os
os.system("cls")

mayor, menor, total = 0,100,0

for i in range(1,4):
    numero = int( input( "Edad "+str(i)+": " ) )
    mayor = numero if numero > mayor else mayor
    menor = numero if numero < menor else menor
    total += numero

print("Mayor edad : "+str(mayor))
print("Menor edad : "+str(menor))

#Con condiconal