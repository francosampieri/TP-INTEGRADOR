from funciones import pedir_int_rango, imprimir_pais, pedir_palabra
from statistics import mean

def buscar_pais(dataset_paises):
    print("=" * 40)
    print("--------BUSCAR PAÍS POR NOMBRE--------")
    print("=" * 40)

    while True:
        pais_encontrado = None

        pais_a_buscar = pedir_palabra("Ingrese el nombre del pais a buscar: ").lower()

        #buscar coincidencia total
        for pais in dataset_paises:
            if pais_a_buscar == pais["nombre"].lower(): 
                pais_encontrado = pais
                break

        if pais_encontrado: 
            imprimir_pais(pais_encontrado)
            return
        
        else:
            #buscar coincidencia parcial
            paises_encontrados = []
            for pais in dataset_paises:
                if pais["nombre"].lower().startswith(pais_a_buscar):
                    paises_encontrados.append(pais)
            
            if not paises_encontrados: print(f"ERROR: No hay ningun pais llamado {pais_a_buscar} ni que comience con esas letras en la base de datos. Intentalo de nuevo")
            else: 
                if len(paises_encontrados) == 1: 
                    imprimir_pais(paises_encontrados[0])
                    return
                else: print(f"ERROR: Hay {len(paises_encontrados)} paises encontrados en nuestra base de datos que comienzan con esas letras. Intenta una busqueda mas precisa")

def filtrar_paises(dataset_paises):
    print("=" * 40)
    print("-------------FILTRAR PAÍSES-------------")
    print("=" * 40)

    eleccion_usuario = input("Ingrese el filtro que desea usar:\n[1]: Por continente\n[2]: Por población\n[3]: Por superficie\n")
    while eleccion_usuario not in ("1","2","3"):
        print("ERROR: Ingrese una opcion valida")
        eleccion_usuario = input("Ingrese el filtro que desea usar:\n[1]: Por continente\n[2]: Por población\n[3]: Por superficie\n")

    if eleccion_usuario == "1": filtrar_por_continente(dataset_paises)
    elif eleccion_usuario == "2": filtrar_por_poblacion(dataset_paises)
    else: filtrar_por_superficie(dataset_paises)

def filtrar_por_continente(dataset_paises):
    print("=" * 41)
    print("------FILTRAR PAÍSES POR CONTINENTE------")
    print("=" * 41)
    
    eleccion_continente = input("Ingrese el continente que desea filtrar\n[1]: África\n[2]: América\n[3]: Asia\n[4]: Europa\n[5]: Oceanía\n")
    while eleccion_continente not in("1", "2", "3", "4", "5"):
        print("ERROR: Ingrese una opcion valida")
        eleccion_continente = input("Ingrese el continente que desea filtrar\n[1]: África\n[2]: América\n[3]: Asia\n[4]: Europa\n[5]: Oceanía\n")

    #dict para vincular la rta del usuario con el continente correspondiente
    dict_continente = {"1": "África", "2": "América", "3": "Asia", "4": "Europa", "5": "Oceanía"}

    #list con todos los paises del continente elegido
    paises_en_continente = [pais for pais in dataset_paises if pais["continente"] == dict_continente[eleccion_continente]]
    if not paises_en_continente: #por si elige un continente sin paises (imposible)
        print(f"No hay paises del continente {dict_continente[eleccion_continente]} en la base de datos.")
        return

    for pais in paises_en_continente:
        imprimir_pais(pais)           

def filtrar_por_poblacion(dataset_paises):
    print("=" * 40)
    print("------FILTRAR PAÍSES POR POBLACIÓN------")
    print("=" * 40)

    print("Ingrese el rango para filtrar la poblacion")
    rango_inferior = pedir_int_rango("Desde: ", 0)
    rango_superior = pedir_int_rango("Hasta: ", rango_inferior+1)

    #crear lista con los paises dentro del rango
    paises_en_rango = [pais for pais in dataset_paises if rango_superior >= pais["poblacion"] >= rango_inferior]
    if not paises_en_rango: #entra si la list esta vacia 
        print(f"No hay ningun país que tenga entre {rango_inferior} y {rango_superior} habitantes en la base de datos")
        return

    for pais in paises_en_rango:
        imprimir_pais(pais) 

def filtrar_por_superficie(dataset_paises):
    print("=" * 41)
    print("------FILTRAR PAÍSES POR SUPERFICIE------")
    print("=" * 41)
    print("Ingrese el rango para filtrar la superficie")
    rango_inferior = pedir_int_rango("Desde: ", 0)
    rango_superior = pedir_int_rango("Hasta: ", rango_inferior+1)

    #crear lista con los paises dentro del rango
    paises_en_rango = [pais for pais in dataset_paises if rango_superior >= pais["superficie"] >= rango_inferior]

    #por si la list esta vacia
    if not paises_en_rango:
        print(f"No hay ningun país que tenga entre {rango_inferior} y {rango_superior} kilometros cuadrados de superficie en la base de datos")
        return

    for pais in paises_en_rango:
        imprimir_pais(pais) 

def ordenar_paises(dataset_paises):
    print("=" * 40)
    print("-------------ORDENAR PAÍSES-------------")
    print("=" * 40)

    print("Ordenar por:")
    print("1 - Nombre")
    print("2 - Poblacion")
    print("3 - Superficie")
    orden = input("Ingrese una opcion: ")
    while orden not in ["1", "2", "3"]:
        print("ERROR: Ingrese [1], [2] o [3]")
        print("Ordenar por:")
        print("1 - Nombre")
        print("2 - Poblacion")
        print("3 - Superficie")
        orden = input("Ingrese una opcion: ")

    if orden == "1": ordenar_por_nombre(dataset_paises)
    elif orden == "2": ordenar_por_poblacion(dataset_paises)
    else: ordenar_por_superficie(dataset_paises)

def ordenar_por_nombre(dataset_paises):
    print("=" * 41)
    print("--------ORDENAR PAÍSES POR NOMBRE--------")
    print("=" * 41)

    tipo_orden = input("De que forma desea ordenarlo:\n[1]: Ascendente\n[2]: Descendente\n")
    while tipo_orden not in ["1", "2"]:
        print("ERROR: Ingresa [1] o [2]")
        tipo_orden = input("De que forma desea ordenarlo:\n[1]: Ascendente\n[2]: Descendente\n")
    
    if tipo_orden == "2": descendente = True
    else: descendente = False

    def obtener_nombre(pais):
        return pais["nombre"]

    dataset_ordenado = sorted(dataset_paises, key=obtener_nombre, reverse= descendente)

    print("\nLista de paises ordenada:\n")
    for pais in dataset_ordenado:
        imprimir_pais(pais)

def ordenar_por_poblacion(dataset_paises):
    print("=" * 40)
    print("------ORDENAR PAÍSES POR POBLACIÓN------")
    print("=" * 40)

    tipo_orden = input("De que forma desea ordenarlo:\n[1]: Ascendente\n[2]: Descendente\n")
    while tipo_orden not in ["1", "2"]:
        print("ERROR: Ingresa [1] o [2]")
        tipo_orden = input("De que forma desea ordenarlo:\n[1]: Ascendente\n[2]: Descendente\n")
    
    if tipo_orden == "2": descendente = True
    else: descendente = False

    def obtener_poblacion(pais):
        return pais["poblacion"]

    dataset_ordenado = sorted(dataset_paises, key=obtener_poblacion, reverse= descendente)

    print("\nLista de paises ordenada:\n")
    for pais in dataset_ordenado:
        imprimir_pais(pais)

def ordenar_por_superficie(dataset_paises):
    print("=" * 41)
    print("------ORDENAR PAÍSES POR SUPERFICIE------")
    print("=" * 41)

    tipo_orden = input("De que forma desea ordenarlo:\n[1]: Ascendente\n[2]: Descendente\n")
    while tipo_orden not in ["1", "2"]:
        print("ERROR: Ingresa [1] o [2]")
        tipo_orden = input("De que forma desea ordenarlo:\n[1]: Ascendente\n[2]: Descendente\n")
    
    if tipo_orden == "2": descendente = True
    else: descendente = False

    def obtener_superficie(pais):
        return pais["superficie"]

    dataset_ordenado = sorted(dataset_paises, key=obtener_superficie, reverse= descendente)

    print("\nLista de paises ordenada:\n")
    for pais in dataset_ordenado:
        imprimir_pais(pais)

def mostrar_estadisticas(dataset_paises):
    print("------------------ESTADÍSTICAS------------------")
    mayor_menor_poblacion(dataset_paises)
    promedio_poblacion(dataset_paises)
    promedio_superficie(dataset_paises)
    paises_por_continente(dataset_paises)

def mayor_menor_poblacion(dataset_paises):
    print("=" * 40)
    print("---PAÍSES CON MENOR Y MAYOR POBLACIÓN---")
    print("=" * 40)

    def obtener_poblacion(pais):
        return pais["poblacion"]

    dataset_ordenado = sorted(dataset_paises, key=obtener_poblacion)
    
    print(f"El país con mayor población en la base de datos es {dataset_ordenado[-1]["nombre"]} con {dataset_ordenado[-1]["poblacion"]} personas")
    print(f"El país con menor población en la base de datos es {dataset_ordenado[0]["nombre"]} con {dataset_ordenado[0]["poblacion"]} personas")

    print() #salto de linea
    input("ENTER para siguiente estadistica ")
    print() #salto de linea

def promedio_poblacion(dataset_paises):
    print("=" * 41)
    print("----------PROMEDIO DE POBLACIÓN----------")
    print("=" * 41)
    
    poblaciones = [pais["poblacion"] for pais in dataset_paises] #crea list con las poblaciones de los paises
    media_poblacion = round(mean(poblaciones), 1)
    print(f"La media de poblacion de los paises en la base de datos es de {media_poblacion} personas")
    print() #salto de linea
    input("ENTER para siguiente estadistica ")
    print() #salto de linea

def promedio_superficie(dataset_paises):
    print("=" * 40)
    print("---------PROMEDIO DE SUPERFICIE---------")
    print("=" * 40)

    superficie = [pais["superficie"] for pais in dataset_paises] #crea list con superficies de los paises
    media_superficie = round(mean(superficie), 1)
    print(f"La media de superficie de los paises en la base de datos es {media_superficie} km cuadrados")
    
    print() #salto de linea
    input("ENTER para siguiente estadistica")
    print() #salto de linea

def paises_por_continente(dataset_paises):
    print("=" * 41)
    print("----------PAÍSES POR CONTINENTE----------")
    print("=" * 41)

    continentes_list = ["África", "América", "Asia", "Europa", "Oceanía"]
    for continente in continentes_list:
        #crea list con los paises en el continente
        paises_en_continente = [pais["continente"] for pais in dataset_paises if pais["continente"] == continente]
        print(f"{continente}: {len(paises_en_continente)} países")

def menu(dataset_paises):
    while True:
        eleccion_menu = input("Ingresa una opcion:\n[1]: Buscar un país por nombre\n[2]: Filtrar países\n[3]: Ordenar países\n[4]: Mostrar estadísticas\n[0]: Salir\n")
        while eleccion_menu not in ["1", "2", "3", "4", "0"]:
            print("ERROR: Ingresa [1], [2], [3] o [4]")
            eleccion_menu = input("Ingresa una opcion:\n[1]: Buscar un país por nombre\n[2]: Filtrar países\n[3]: Ordenar países\n[4]: Mostrar estadísticas\n")
        
        if eleccion_menu == "1": buscar_pais(dataset_paises)
        elif eleccion_menu == "2": filtrar_paises(dataset_paises)
        elif eleccion_menu == "3": ordenar_paises(dataset_paises)
        elif eleccion_menu == "4": mostrar_estadisticas(dataset_paises)
        else:
            print("Muchas gracias")
            break
        
        input("ENTER para volver al menú ")
        print() #salto de linea

#main
#CREACION DEL DATASET
dataset_paises = []
with open("paises.csv", "r", encoding="utf-8") as paises: #encoding utf-8 porque el csv tiene acentos y ñ
    for linea in paises:
        nombre, poblacion, superficie, continente = linea.strip().split(",")
        dataset_paises.append({
            "nombre": nombre,
            "poblacion": int(poblacion),
            "superficie": int(superficie),
            "continente": continente
        })
    
menu(dataset_paises)