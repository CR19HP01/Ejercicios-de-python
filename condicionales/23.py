import os
os.system("cls")

matematica = int( input( "Nota de Matemática : " ) )
fisica = int( input( "Nota de  Física    : " ) )

propinaM = 3 if matematica > 17 else 1 * matematica 
propinaF = 2 if fisica > 15 else 0.5

promedio = (matematica + fisica)/ 2 
if promedio > 16 : print("Su promedio es ",promedio, "por eso su papá le obsequio un reloj") 
else : print("Su prommedio es ",promedio,"por eso su papá no le obsequio el reloj")
print(f'Su propina de matemática es S/. {propinaM} y la de física es S/. {propinaF} en total resivirá S/. {propinaF + propinaM}')
