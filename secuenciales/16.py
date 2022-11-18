import os
os.system("cls")
 
tarifaHoraria = int( input( "Tarifa horaria : " ) )
totalHoras = int( input( "Número total de horas trabajadas : " ) )

sueldoBasico = tarifaHoraria * totalHoras 
sueldoBruto = sueldoBasico * 0.2
sueldoNeto = sueldoBruto * 0.1

print( f'Sueldo Básico : {sueldoBasico}\nSueldo Bruto : {sueldoBruto}\nSueldo Neto : {sueldoNeto}')

#preguntar si esta 