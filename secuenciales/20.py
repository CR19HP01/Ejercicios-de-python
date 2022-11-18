import os 
os.system("cls")

numero = int( input( "Cantidad de dinero : ") )
 
#billetes
b200cociente = numero // 200 
b200resto = numero % 200

b100cociente = b200resto // 100
b100resto = b200resto % 100

b50cociente = b100resto // 50
b50resto = b100resto % 50

b20cociente = b50resto // 20
b20resto = b50resto % 20

b10cociente = b20resto // 10
b10resto = b20resto % 10

#monedas
m5cociente = b10resto // 5
m5resto = b10resto % 5

m2cociente = m5resto // 2
m2resto = m5resto % 2

m1cociente = m2resto // 1 
m1resto = m2resto % 1

print( "Cantidad de billetes de 200 : ",b200cociente)
print( "Cantidad de billetes de 100 : ",b100cociente)
print( "Cantidad de billetes de 50 : ",b50cociente)
print( "Cantidad de billetes de 20 : ",b20cociente)
print( "Cantidad de billetes de 10 : ",b10cociente)
print( "Cantidad de monedas de 5 : ",m5cociente)
print( "Cantidad de monedas de 2 : ",m2cociente)
print( "Cantidad de monedas de 1 : ",m1cociente)