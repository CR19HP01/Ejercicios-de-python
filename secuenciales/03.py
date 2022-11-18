import os
os.system("cls")

numeroKilometro = int( input("Kilometro : ") )
numeroPies = int( input("Pies : "))
numeroMillas = int( input("Millas : "))

respuestaMetro = (numeroKilometro / 1000) + (numeroPies / 3.2808) + (numeroMillas * 1609)
respuestaYarda = (numeroKilometro*1000*3.2808)/3 + (numeroPies / 3) + (numeroMillas * 1609 * 3.2808)/3

print()
print( f'Solución en metros : {respuestaMetro} m ')
print( f'Solucion en yardas : {respuestaYarda} yd ')

2187.8 