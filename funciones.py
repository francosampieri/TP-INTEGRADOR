def pedir_int_rango(mensaje, limite_inf = -float("inf"), limite_sup = float("inf")):
    """
    Pide un numero entero y valida que este dentro dentro del rango solicitado\n
    mensaje = mensaje a mostrar en input\n
    limite_inf = limite inferior del rango\n
    limite_sup = limite superior del rango\n
    retorna int
    """
    while True:
        n = input(mensaje)
        try: n = int(n)
        except: 
            print("ERROR: Ingresa un numero entero")
            continue
        if not limite_inf<=n<=limite_sup:
            print(f"ERROR: El numero ingresado no esta entre {limite_inf} y {limite_sup}")
            continue
        return n

def pedir_palabra(mensaje):
    """Pide una palabra que no tenga simbolos ni numeros\n
    mensaje = mensaje del input
    """
    string = "1,." #especifico para evitar que el usuario ingrese esa cadena
    while not string.isalpha():
        if string != "1,.": print("ERROR: Ingrese una cadena de solo letras")
        string = input(mensaje)
    return string

def imprimir_pais(pais):
    """Recibe dict de pais e imprime sus datos con formato"""
    print(f"----------{pais["nombre"]}-----------")
    print(f"Poblacion: {pais["poblacion"]}")
    print(f"Superficie: {pais["superficie"]} km cuadrados")
    print(f"Continente: {pais["continente"]}")
    print() #salto de linea