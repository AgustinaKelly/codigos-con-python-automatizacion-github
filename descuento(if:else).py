valorCompra= int(input('Ingrese el valor de la compra: '))


if valorCompra <= (50000):
        print('El monto que tiene que abonar es: ', valorCompra)
else:
        porcentaje = (valorCompra * 0.10)
        resultado = (valorCompra - porcentaje)
        print('El monto abonar con descuento es: ', resultado)


#agregue un comentario
    
