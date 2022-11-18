articulo = int( input( "Articulo : " ) )
precio = int( input( "Precio del articulo : " ) ) 

importeCompra = articulo * precio
descuento1 = precio * 0.15
descuento2 = (importeCompra - descuento1) * 0.15
importePago = importeCompra - descuento2 #Resta total

print( "Importe de la compra : ",importeCompra)
print( "Descuento : ",descuento2)
print( "Importe de pago : ",importePago)
