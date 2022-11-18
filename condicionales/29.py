import os
os.system("cls")

canTotal = int( input("Horas trabajadas : " ) ) 
sueldo = int( input("Sueldo : " )) 

horaNormal = sueldo/(30 * 8)
horaExtra = horaNormal * 0.2

if canTotal <= 48 or canTotal > 48 : 
    horaNormal
    sueldoBruto = canTotal * (horaExtra or horaNormal) + sueldo

#else :
#    horaExtra
#    sueldoBruto = canTotal * (horaExtra or horaNormal) + sueldo


#sueldoBruto = canTotal * (horaExtra or horaNormal) + sueldo

descuento = (0.11 if sueldoBruto > 1500 else 0) * canTotal

print(f'Pago por hora : S/. {horaNormal}')
print(f'Sueldo bruto  : S/. {sueldoBruto}')
print(f'Descuento     : S/. {descuento }')
print(f'Total a pagar : S/. {sueldoBruto - descuento}')