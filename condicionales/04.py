practica1 = int( input( "1 Práctica : " ) )
practica2 = int( input( "2 Práctica : " ) )
practica3 = int( input( "3 Práctica : " ) )

if practica3 >= 10: aumento = practica3 + 2; promedio = (practica1 + practica2 + aumento)/3; print("Promedio Final : ",promedio)
else: promedio = (practica1 + practica2 + practica3) / 3; print("Promedio Final : ",promedio)