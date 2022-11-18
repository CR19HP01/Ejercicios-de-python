import os
os.system("cls")

empleadoHijo = int( input("Número de hijos : " ) )

sueldoBruto = 100

if empleadoHijo > 1 : bonificacion = (12.5 * sueldoBruto) + (40 * empleadoHijo)
else : bonificacion = 0.1 * sueldoBruto

print(f'Bonificación : {bonificacion}')
print(f'Sueldo neto : {sueldoBruto + bonificacion}')