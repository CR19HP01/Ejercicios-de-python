import os
os.system("cls")

juan = int( input( "Cantidad aportado por Juan : " ) )
rosa = int( input( "Cantidad aportado por Rosa : " ) )
daniel = int( input( "Cantidad aportado por Daniel : " ) )

cambioDolar = daniel * 3
capitalTotal = juan + rosa + cambioDolar
pJuan = juan * 100 / capitalTotal
pRosa = rosa * 100 / capitalTotal
pDaniel = cambioDolar* 100 / capitalTotal


print( f'Capital total : {capitalTotal} $')
print( f'Porcentaje aportado por Juan : {pJuan} %')
print( f'Porcentaje aportado por Rosa: {pRosa} %')
print( f'Porcentaje aportado por Daniel : {pDaniel} %')
