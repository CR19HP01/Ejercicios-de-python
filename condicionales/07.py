n1 = int( input( "Numero 1 : " ) ) 
n2 = int( input( "Numero 2 : " ) )
n3 = int( input( "Numero 3 : " ) )

max( n1,n2,n3 ) 
min( n1,n2,n3 )

print( "Número intermedio : ",n1 + n2 + n3 - max(n1,n2,n3) - min(n1,n2,n3))

