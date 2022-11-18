unidad = int ( input ("Unidad : ") )
operacionCentimetro = unidad * 100
operacionPulgada = operacionCentimetro * 2.54
operacionPie = operacionPulgada * 12
operacionYarda = operacionPie * 3


print( f'{unidad} Metros a {operacionCentimetro} Centímetros' )
print( f'{unidad} Pies a {operacionPie} Pulgadas' )
print( f'{unidad} Yardas a {operacionYarda} Pies')
print( f'{unidad} Pulgadas a {operacionPulgada} Centímetros')