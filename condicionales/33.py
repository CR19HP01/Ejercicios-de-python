import os
os.system("cls")

minutosTarde = int( input("Minutos de tardanza : " ) )
observaciones = int( input("Observaciones : ") ) 

puntajeMin = 10 if minutosTarde == 0 else 0 if minutosTarde > 9 else 8 if 1 < minutosTarde <= 2 else 6 if 3 <= minutosTarde <=5 else 4  
puntajeObs = 10 if observaciones == 0 else 0 if observaciones > 3 else 8 if observaciones == 1 else 5 if observaciones == 2 else 1 

puntajeTotal = puntajeMin + puntajeObs
bonificaciones = (2.5 if puntajeTotal < 11 else 12.5 if puntajeTotal >= 20 else 5 if 11 <= puntajeTotal <= 13 else 7.5 if 14 <= puntajeTotal <=16 else 10 ) * puntajeTotal

print(f'Puntaje por puntualidad : {puntajeMin} ')
print(f'Puntaje por rendimiento : {puntajeObs} ')
print(f'Puntaje total           : {puntajeTotal} ')
print(f'Bonificación            : S/. {bonificaciones}')
print()