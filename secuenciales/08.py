PI = 3.14
radio = int( input("Radio: ") )
altura = int( input("Altura: ") )

areaBase = PI * ( radio**2 ) 
areaLateral = 2 * PI * radio * altura
areaTotal = areaBase + areaLateral

print( f'Área Base : {areaBase} cm²')
print( f'Área Lateral : {areaLateral} cm²')
print( f'Área Total : {areaTotal} cm² ')