dataset_paises = []
with open("paises.csv", "r", encoding="utf-8") as paises:
    for linea in paises:
        nombre, poblacion, superficie, continente = linea.strip().split(",")
        dataset_paises.append({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})

print(dataset_paises)