#definir las constantes
precio_sencilla = 20000
precio_doble = 25000
precio_triple = 28000
precio_tarjeta = 0.07

#funcion para calcular el precio
def calcular_precio(tipo_hamburguesa, medio_pago, cantidad):

#definir los precios segun tipos de hamburguesas
    if tipo_hamburguesa ==1:
        precio = precio_sencilla
        descripcion = "sencilla"
    elif tipo_hamburguesa ==2:
        precio = precio_doble
        descripcion = "doble"
    elif tipo_hamburguesa ==3:
        precio = precio_triple
        descripcion = "triple"
    else:
        return None #tipo de hamburguesa no valida!

#calcular el total sin cargos
    total_sin_cargo = precio * cantidad

#aplicar impuestos si el medio de pago es tarjeta
    if medio_pago == 1:

    impuesto = round(total_sin_cargo * impuesto_tarjeta)
    else:
    impuesto = 0
    total = round(total_sin_cargo + impuesto)

#restornar datos relevantes
    return descripcion, precio, cantidad, impuesto, total

#funcion para generar mensaje
def generar_mensaje(descripcion, precio, cantidad, impuesto, total):
    return (f"tipo de hamburguesa: {descripcion}\n"
            f"precio: ${precio}\n"
            f"cantidad: ${cantidad}\n"
            f"impuesto: ${impuesto}\n"
            f"total: ${total}\n")

#funcion para validar los datos
def 1 <= tipo_hamburguesa <= 3 and 1 <= medio_pago <= 2 and cantidad > 0:
    resultado = calcular precio(tipo_hamburguesa, medio_pago, cantidad)

#print("resultado: ",resultado)
    descripcion, precio, cantidad, impuesto, total = resultado
    mensaje = generar_mensaje(descripcion, precio,cantidad, impuesto, total)
    print("_____________________________\n"+ mensaje)
 else
    print("verifique")

 #entradas
tipo_hamburguesa = int(input("ingrese tipo de hamburguesa \n1. sencilla \n2. doble \n3. triple \n"))
medio_pago = int(input("ingrese medio de pago \n1. tarjeta \n2. otro \n"))
cantidad = int(input("ingrese la cantidad: "))

 #salidas
 validar_datos(tipo_hamburguesa,medio_pago,cantidad)