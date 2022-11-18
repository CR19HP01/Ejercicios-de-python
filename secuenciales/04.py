pie = int( input( "Ingrese cantidad de pies : " ) )
pulgada = int( input( "Ingrese cantidad de pulgada : " ) )

pieMetro = pie * 0.30
pulgadaMetro = pulgada * 0.254

estatura = pieMetro + pulgadaMetro

print( "Estatura : ",estatura,"m")