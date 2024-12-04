from enum import Enum, auto

"""
1. Calcular precio y tipo en funcion de la edad y guardarlo en algun sitio para luego... OK

2. Pedir la edad -> OK
    Validar que sea entero positivo -> OK
    Pedir edades hasta que se introduzca ""

3. Calcular el precio total del grupo OK

4. mostrar el precio total y el desglose por tipo de entrada OK 

"""

precioTotal = 0
grupoPersonas = []


class Entrada(Enum):
    GRATUITA = 0
    NINYOS = 14
    ADULTOS = 23
    JUBILADOS = 18

def calculoPrecioYTipoBillete(edad: int):
    precio = 0
    if edad >=3 and edad <= 12:
        tipo = Entrada.NINYOS
        precio = tipo.value
    elif edad >= 13 and edad < 65:
        tipo = Entrada.ADULTOS
        precio = tipo.value
    elif edad >= 65:
        tipo = Entrada.JUBILADOS
        precio = tipo.value
    else:
        tipo = Entrada.GRATUITA
        precio = tipo.value

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
    for precio, tipo in grupoPersonas:
        precioTotal += precio
        print(f"Precio: {precio}, tipo de entrada: {tipo}")

    print(f"Precio total: {precioTotal}")


"""
Bucle de peticion de edades, para cada edad debe imprimir precio y tipo
y acabar cuando se introduzca ""
"""
while True:
    edad = input("Cuantos aÃ±os tienes: ")
    if edad == "":
        break
    elif validaEnteroPositivo(edad):
        grupoPersonas.append(calculoPrecioYTipoBillete(int(edad)))
        infoFactura(grupoPersonas)

print(grupoPersonas)




