"""
1. Calcular precio y tipo en funcion de la edad y guardarlo en algun sitio para luego... OK

2. Pedir la edad -> OK
    Validar que sea entero positivo -> OK
    Pedir edades hasta que se introduzca "" OK 

3. Calcular el precio total del grupo OK 

4. mostrar el precio total y el desglose por tipo de entrada OK 

5. Reiniciar la opción del bucle

"""
grupoPersonas = []
tipos_entradas = ["GRATUITA", "NINYOS", "ADULTOS", "JUBILADOS"]
precios = [0, 14, 23, 18]

edades_umbral = [3, 13, 65, float('inf')]


def calculoPrecioYTipoBillete(edad: int):
    # TODO: Poner esta funcion de forma que los indices encajen con el
    precio = 0
    tipo = 0

    for i, edad_umbral in enumerate(edades_umbral):
        if edad < edad_umbral:
            precio = precios[i]
            tipo = i
            break
            

    return precio, tipo

def validaEnteroPositivo(dato: str):
    """
    Debe devolver True si dato es entero mayor o igual que cero
                  False en otro caso
    """
    res = False
    try:
        int(dato)
        res = True
    except ValueError:
        res = False
    return res

def infoFactura(grupoPersonas):
    precioTotal = 0
    contadores_entradas = [0, 0, 0, 0]
    totales_entradas = [0, 0, 0, 0]
    for precio, tipo in grupoPersonas:
        precioTotal = precioTotal + precio
        contadores_entradas[tipo] += 1
        totales_entradas[tipo] += precio
    return precioTotal, contadores_entradas, totales_entradas


def imprimeFactura(tipos_entradas, contadores_entradas,totales_entradas):
    
    for i, tipo in enumerate(tipos_entradas):
        print(f"{contadores_entradas[i]:2d} entradas {tipo.lower()}: {totales_entradas[i]:6.2f} €")


def continuar():
    respuesta = input("Desea emitir otra factura?: s/n  ")
    if respuesta != "s" or respuesta != "n":
        respuesta = input("Desea emitir otra factura?: s/n  ")
    respuesta.lower()

    return respuesta 
"""
Bucle de peticion de edades, para cada edad debe imprimir precio y tipo
y acabar cuando se introduzca ""
"""
while True:
    edad = input("Cuantos años tienes: ")
    if edad == "":
        precioTotal, contadores_entradas, totales_entradas = infoFactura(grupoPersonas)
        imprimeFactura(tipos_entradas, contadores_entradas, totales_entradas)
        print("-" * 25)
        num_entradas = len(grupoPersonas)
        print(f"Numero de entradas: {num_entradas:03d}")
        print(f"Total a pagar.....: {precioTotal:.2f} €")
        break

    elif validaEnteroPositivo(edad):
        grupoPersonas.append(calculoPrecioYTipoBillete(int(edad)))
    
   
       
       
    
    

# grupoPersonas = [(0, 0), (23, 2), (23, 2), (18, 3), (18, 3)]









  
