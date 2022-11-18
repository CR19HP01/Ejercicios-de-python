import os 
os.system("cls")

n = int( input("Número : " ) )

if n >= 4 :
    for x in range(1, n + 1) :
        if x == 1 or x == n :
            for  o in range(2 * n) : 
                print("* ", end="") # finalizar y dar un salto de linea
        else : 
            for p in range( 1, 2*n + 1):
                if p == 1 or p == 2*n : print("* ", end="")
                else : print("  ", end = "")
        print()
    print()
else :
    n = int( input("Ingrese de un número que sea mayor o igual a 4 : ") )
    for x in range(1, n + 1) :
        if x == 1 or x == n :
            for  o in range(2 * n) : 
                print("* ", end="") # finalizar y dar un salto de linea
        else : 
            for p in range( 1, 2*n + 1):
                if p == 1 or p == 2*n : print("* ", end="")
                else : print("  ", end = "")
        print()
    print() 