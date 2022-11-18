import os
os.system("cls")

empleado = int( input( "Ingresar codigo de tres cifras : " ) )

bdiv2 = empleado % 2 == 0
bdiv3 = empleado % 3 == 0
bdiv5 = empleado % 5 == 0

tipo = ""
if bdiv2 and bdiv3 and bdiv5 : tipo = "Administrativo"
if not bdiv2 and bdiv3 and bdiv5 : tipo = "Directivo"
if bdiv2 and not bdiv3 and not bdiv5 : tipo ="Vendedor"
if not bdiv2 and not bdiv3 and not bdiv5 : tipo = "Seguridad"

print( f'Tipo : {tipo}' )
print()


