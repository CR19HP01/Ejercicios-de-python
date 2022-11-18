import os
os.system("cls")

def hora(tiempo):
	"""
		Este metodo convierte el formato 24 al formato 12
		Ejemplo:	"00:32" es "12:32 AM"
					"13:33" es "01:33 PM"
	"""
	formato = tiempo.split (":")
	if (len(formato) == 0) or (len(formato) > 3):
		return tiempo
 
	hour = int(formato[0]) % 24
	isam = (hour >= 0) and (hour < 12)
 
	if isam:
		formato[0] = ('12' if (hour == 0) else "%02d" % (hour))
	else:
		formato[0] = ('12' if (hour == 12) else "%02d" % (hour-12))
 
	return ':'.join (formato) + (' AM' if isam else ' PM')
 
cambio = input("Cambio de 24h a 12h : " ) 
c = hora(cambio)
print(f'Formato de 24h es {cambio} y cambia a formato de 12h {c}')