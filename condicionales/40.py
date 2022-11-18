import os
os.system("cls")

print("MATEMÁTICA")
matePc1 = float( input("Práctica calificada 1 : " ) ) 
matePc2 = float( input("Práctica calificada 2 : " ) ) 
matePc3 = float( input("Práctica calificada 3 : " ) )
mateEP = float( input("Examen parcial        : ") )
mateEF = float( input("Examen final          : ") )
print()

if matePc1 : pMpc1 = matePc1 * 0.1 
if matePc2 : pMpc2 = matePc2 * 0.2
if matePc3 : pMpc3 = matePc3 * 0.1
if mateEP : pM_ep = mateEP * 0.3
if mateEF : pM_ef = mateEF * 0.3

promedioFinalM = pM_ef + pM_ep + pMpc2 + pMpc1 + pMpc3

if 20 >= promedioFinalM >= 13 : print("Curso de Matemática : APROBADO")
else : print("Curso de Matemática : DESAPROBADO")

print("Promedio Final : ",promedioFinalM)

print()
print("FÍSICA")
fiPc1 = float( input("Práctica calificada 1 : " ) ) 
fiPc2 = float( input("Práctica calificada 2 : " ) ) 
fiPc3 = float( input("Práctica calificada 3 : " ) )
fiEP = float( input("Examen parcial        : ") )
fiEF = float( input("Examen final          : ") )
print()

if fiPc1 : pFpc1 = fiPc1 * 0.2
if fiPc2 : pFpc2 = fiPc2 * 0.2
if fiPc3 : pFpc3 = fiPc3 * 0.2
if fiEP : pF_ep = fiEP * 0.2
if fiEF : pF_ef = fiEF * 0.2

promedioFinalF = pF_ef + pF_ep + pFpc2 + pFpc1 + pFpc3

if 20 >= promedioFinalF >= 13 : print("Curso de Física : APROBADO")
else : print("Curso de Física : DESAPROBADO")

print("Promedio Final : ",promedioFinalF)


print()
print("QUÍMICA")
quiPc1 = float( input("Práctica calificada 1 : " ) ) 
quiPc2 = float( input("Práctica calificada 2 : " ) ) 
quiPc3 = float( input("Práctica calificada 3 : " ) )
quiEP = float( input("Examen parcial        : ") )
quiEF = float( input("Examen final          : ") )
print()

if quiPc1 : pQpc1 = quiPc1 * 0.1
if quiPc2 : pQpc2 = quiPc2 * 0.3
if quiPc3 : pQpc3 = quiPc3 * 0.1
if quiEP : pQ_ep = quiEP * 0.25
if quiEF : pQ_ef = quiEF * 0.25

promedioFinalQ = pQ_ef + pQ_ep + pQpc2 + pQpc1 + pQpc3

if 20 >= promedioFinalQ >= 13 : print("Curso de Química : APROBADO")
else : print("Curso de Química : DESAPROBADO")

print("Promedio Final : ",promedioFinalQ)