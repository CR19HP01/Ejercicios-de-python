import os 
os.system("cls")

angulo = int ( input("Ingrese el ángulo dado en  grados : ") )

if angulo > 0 and angulo < 90  : print( "La clasificación del ángulo es : Agudo" ) 
elif angulo == 0 : print ("La clasificación del ángulo es : Nulo")
elif angulo == 90 : print("La clasificación del ángulo es : Recto")

#if angulo == 0 : print("La clasificación del ángulo es : Nulo")
#elif angulo >0 and angulo < 90 : print("La clasificación del ángulo es : Agudo")
#else: print("La clasificación del ángulo es : Recto")

if 90< angulo < 180 : print("La clasificación del ángulo es : Obtuso")
elif angulo == 180 : print("La clasificación del ángulo es : Llano")

if 180 < angulo < 360 : print("La clasificación del ángulo es : Cóncavo")
elif angulo == 360 : print("La clasificación del ángulo es : Completo")

