def Continuar():
    while True:
        eleccion = input("\nDesea continuar (1-Sí / 2-No): ")
        if eleccion == "1":
            return True
        elif eleccion == "2":
            return False
        else:
            print(" Error: solo se puede ingresar '1' para Sí o '2' para No.")


def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("ERROR: Debe ingresar un numero.")


def buscar_pais(dataset_paises):
    continuar = True
    while continuar: 
        pais_Encontrado = None
        pais_a_Buscar = input("Ingrese el nombre del pais a buscar: ").lower()
        for pais in dataset_paises:
            if pais_a_Buscar == pais["nombre"].lower(): 
                pais_Encontrado = pais
                break

        if pais_Encontrado:
            print("\nPaís encontrado:")
            print(f"Nombre: {pais_Encontrado['nombre']}")
            print(f"Poblacion: {pais_Encontrado['poblacion']}")
            print(f"Superficie: {pais_Encontrado['superficie']} km(Cuadrados)")
            print(f"Continente: {pais_Encontrado['continente']}")
        else:
            print("No se encontro ningun pais con ese nombre.")
            
        continuar = Continuar()
                #RETORNAR AL MENU PRINCIPAL



def Ordenar_paises(dataset_paises):
    seguir = True
    while seguir:
        print("\nOrdenar por:")
        print("1 - Nombre")
        print("2 - Poblacion")
        print("3 - Superficie")
        orden = input("Ingrese una opcion: ")

        if orden == "1":
            print("\nOrdenar la lista por Nombre\n")
            tipo_orden = input("Desea ordenarlo de forma ascendente (1) o descendente (2): ")

            if tipo_orden == "1":
                ascendente = True
            else:
                ascendente = False

            def obtener_nombre(pais):
                return pais["nombre"]

            dataset_paises.sort(key=obtener_nombre, reverse=not ascendente)

            print("\nLista de paises ordenada:\n")
            for pais in dataset_paises:
                print(f"Nombre: {pais['nombre']}")
                print(f"Poblacion: {pais['poblacion']}")
                print(f"Superficie: {pais['superficie']} km(Cuadrados)")
                print(f"Continente: {pais['continente']}")
            
            seguir = Continuar()

        elif orden == "2":
            print("\nOrdenar la lista por Poblacion\n")
            tipo_orden = input("Desea ordenarlo de forma ascendente (1) o descendente (2): ")

            if tipo_orden == "1":
                ascendente = True
            else:
                ascendente = False

            def obtener_poblacion(pais):
                return int(pais["poblacion"])

            dataset_paises.sort(key=obtener_poblacion, reverse=not ascendente)

            print("\nLista de paises ordenada:\n")
            for pais in dataset_paises:
                print(f"Nombre: {pais['nombre']}")
                print(f"Poblacion: {pais['poblacion']}")
                print(f"Superficie: {pais['superficie']} km(Cuadrados)")
                print(f"Continente: {pais['continente']}")
            
            seguir = Continuar()

        elif orden == "3":
            print("\nOrdenar la lista por Superficie\n")
            tipo_orden = input("Desea ordenarlo de forma ascendente (1) o descendente (2): ")

            if tipo_orden == "1":
                ascendente = True
            else:
                ascendente = False

            def obtener_superficie(pais):
                return float(pais["superficie"])

            dataset_paises.sort(key=obtener_superficie, reverse=not ascendente)

            print("\nLista de paises ordenada:\n")
            for pais in dataset_paises:
                print(f"Nombre: {pais['nombre']}")
                print(f"Poblacion: {pais['poblacion']}")
                print(f"Superficie: {pais['superficie']} km(Cuadrados)")
                print(f"Continente: {pais['continente']}")
            
            seguir = Continuar()
        #RETORNAR AL MENU PRINCIPAL
        else:
            print("Error: opción no válida. Intente nuevamente.")


#Main
dataset_paises = []
with open("paises.csv", "r", encoding="utf-8") as paises:
    for linea in paises:
        nombre, poblacion, superficie, continente = linea.strip().split(",")
        dataset_paises.append({
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        })

#buscar_pais(dataset_paises)
Ordenar_paises(dataset_paises)
