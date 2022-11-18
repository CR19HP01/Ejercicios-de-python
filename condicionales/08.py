import os
os.system("cls")

propina = 20

examen1 = int( input("Examen 1 : ") )
examen2 = int( input("Examen 2 : ") )
examen3 = int( input("Examen 3 : ") )

if examen1 > 10 :  propina += 5
if examen2 > 10 : propina += 5
if examen3 > 10 : propina += 5

print(f'Total : {propina}')