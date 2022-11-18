import os
os.system("cls")

gigabytes = int( input("Capacidad de un disco duro: " ) )

convertirMegabytes = gigabytes * 1024
convertirKilobytes = convertirMegabytes * 1024
convertirBytes = convertirKilobytes * 1024

print( f'{gigabytes} Gigabytes = {convertirMegabytes} Megabytes')
print( f'{gigabytes} Gigabytes = {convertirKilobytes} Kilobytes')
print( f'{gigabytes} Gigabytes = {convertirBytes} bytes')

