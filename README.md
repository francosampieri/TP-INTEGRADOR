# TP-INTEGRADOR
Proyecto: Análisis de Países en Python  

## Descripción del programa  
Este programa permite gestionar y analizar información de distintos países a partir de un archivo CSV que contiene su **nombre, poblacion, superficie (km cuadrados) y continente**.  
A través de un menú interactivo, el usuario puede **buscar, filtrar, ordenar y obtener estadísticas** sobre los países del dataset.  

El código utiliza **listas, diccionarios, funciones modulares y validaciones de entrada**, buscando mantener una estructura limpia, clara y reutilizable.  

## Funcionalidades principales  
-  **Buscar país por nombre:** permite ingresar el nombre (o el inicio del nombre) de un país y obtener su información completa.  
-  **Filtrar países:** por continente, rango de población o rango de superficie.  
-  **Ordenar países:** por nombre, población o superficie, tanto en forma ascendente como descendente.  
-  **Mostrar estadísticas:** calcula y muestra:
  - País con mayor y menor población.  
  - Promedio de población.  
  - Promedio de superficie.  
  - Cantidad de países por cada continente.  


## Instrucciones de uso  
Ejecuta el programa principal **main.py**

Se mostrará el siguiente menú principal:

 -[1]: Buscar un país por nombre
 -[2]: Filtrar países
 -[3]: Ordenar países
 -[4]: Mostrar estadísticas
 -[0]: Salir
Ingrese la opción deseada y siga las instrucciones del programa.

Presione ENTER cuando el programa lo indique para continuar o volver al menú principal.

## Ejemplos de entradas y salidas
-  [1] Buscar un país por nombre
  - **ENTRADA**
    Arg
  - **SALIDA**
    ----------Argentina-----------
    Poblacion: 45376763
    Superficie: 2780400 km cuadrados
    Continente: América
    
    ENTER para volver al menú

-  [2] Filtrar países
  - **ENTRADA**
    1 (por continente)
  - **SALIDA**
    =========================================
    ------FILTRAR PAÍSES POR CONTINENTE------
    =========================================
    Ingrese el continente que desea filtrar
    [1]: África
    [2]: América
    [3]: Asia
    [4]: Europa
    [5]: Oceanía
    
  - **ENTRADA**
  5 (Oceania)
  - **SALIDA**
  ----------Australia-----------
  Poblacion: 25788217
  Superficie: 7692024 km cuadrados
  Continente: Oceanía
  
  ----------Nueva Zelanda-----------
  Poblacion: 5265100
  Superficie: 268021 km cuadrados
  Continente: Oceanía

## Participación de los integrantes
- **Franco Sampieri**
  - Creación de funcion *filtrar_países*
  - Creación de README.me

- **Renzo Victoria**
  - Creacion de funcion *buscar_país*
  - Edición de video

- **Tomas Martinez**
  - Creacion de función *ordenar_paises*
  - Creacion de menú

- **Mauro Di Pietro**
  - Creacion de funcion *mostrar_estadisticas*
  - Testeo de codigo y corrección

- **Alam Gonzalez**
  - Creacion de *funciones.py*
  - Creación de mayor parte del informe

- **Felipe Videla**
  - Creación de csv y dataset
  - Creación de esquema del flujo
 
