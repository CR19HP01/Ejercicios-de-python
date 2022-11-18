import os 
os.system("cls")

horaAusencia = float( input("Horas de ausencia : " ) )
defectuoso = int( input( "Tornillos defectuosos producidos : " ) ) 
noDefectuoso = int( input( "Tornillos no defectuosos producidos : " ) ) 

grado = ""
if horaAusencia <= 1.5 :   grado = "Grado 7"
elif defectuoso < 300 : grado = "Grado 8"
elif noDefectuoso > 10000 : grado = "Grado 9"

if horaAusencia <= 1.5 and defectuoso < 300 : grado = "Grado 12"
if horaAusencia <= 1.5 and noDefectuoso > 10000 : grado = "Grado 13"
if defectuoso < 300 and noDefectuoso > 10000 : grado = "Grado 15"

if horaAusencia <= 1.5 and defectuoso < 300 and noDefectuoso > 10000 : grado = "Grado 20"

print()
print("Grado de eficiencia : ",grado)

#bHoraAusencia = float( input("Horas de Ausencia : ") ) <= 1.5
#bTDefectuosos = int( input("Tornillos Defectuosos :") ) < 300
#bTDefectuosos = int( input( "Tornillos buenos " ) ) > 10000

#grado = 0
#if not bHorasAusencia and not bTDefectuosos and not btBuenos :  grado = 5
#elif not bHorasAusencia and bTDefectuosos and bTBuenos : grado = 7
#if bHorasAusencia and not bTDefectuosos and bTBuenos : grado = 8
#if bHorasAusencia and bTDefectuosos and not bTBuenos : grado = 12
#if bHorasAusencia and not bTDefectuosos and bTBuenos : grado = 13
#if not bHorasAusencia and  bTDefectuosos and bTBuenos : grado = 15
#if bHorasAusencia and bTDefectuosos and bTBuenos : grado = 20

#print('Grado : {grado}')
#print()