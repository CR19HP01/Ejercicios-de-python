import os
os.system("cls")

cadena = input("Texto : ")

mayuscula = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S","T", "U", "V", "W", "X", "Y","Z"]
minuscula = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u", "v", "w", "x", "y", "z"]

mayusCadena = ""
for l in cadena :
    if l in mayuscula : l = minuscula[ ( mayuscula.index(l) ) ]
    mayusCadena += l 

mayusCadena = mayuscula[ minuscula.index(mayusCadena[0])] + mayusCadena[1:]

print(f'Texto en minuscula : {mayusCadena}')
