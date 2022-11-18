def ltrim(texto = "") : 
    if texto =="" : return ""
    while x < len(texto) and texto[x] == " " : x += 1
    return texto[x:]

def rtrim(texto ="") :
    if texto =="" :return ""
    x = len(texto) -1
    while x > 0 and texto[x] == "" : x -= 1 
    return texto[:x + 1]

def trim(texto ="") :
    if texto =="" : return ""
    return rtrim ( ltrim(texto) )

texto = input("palaras : ")
v=ltrim(input("Texto : "))