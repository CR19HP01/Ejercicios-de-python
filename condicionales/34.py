import os
os.system("cls")

peso = int( input("Peso en kilos : " ) )
estatura = float( input("Estatura en metros : " ) ) 

IMC = peso / estatura ** 2

gradoObesidad = "Delgado" if IMC < 20 else "Obesidad" if IMC > 27 else "Normal" if 20 <= IMC < 25 else "Sobrepeso"

print(f'Grado de obesidad : {gradoObesidad}')