# TPI - Programacion 1

import csv

paises = []

# Funciones de validacion
def pedir_entero_positivo(mensaje):  # Valido que sea numero y mayor a 0
    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            input("\nError, asegurate de ingresar un valor numerico, presiona Enter para volver a intentarlo.. ")
        else:
            if numero <= 0:
                input("\nError, asegurate de ingresar un valor mayor a 0, presiona Enter para volver a intentarlo.. ")
            else:
                return numero

def pedir_string(mensaje):  # Valido que no sea un campo vacio
    while True:
        valor = input(mensaje).strip()
        if len(valor) == 0:
            input("\nError, no puedes ingresar un campo vacio, presiona Enter para volver a intentarlo.. ")
        else:
            return valor

# Lectura del CSV
def cargar_csv():  # Leo el archivo CSV y cargo los paises en la lista
    try:
        with open("paises.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })
        print(f"\nSe cargaron {len(paises)} paises correctamente.")
    except FileNotFoundError:
        input("\nError, no se encontro el archivo paises.csv, presiona Enter para continuar.. ")
    except Exception as e:
        input(f"\nError al leer el CSV: {e}, presiona Enter para continuar.. ")

# Mostrar todos los paises
def mostrar_todos():  # Muestro todos los paises con sus datos
    if len(paises) == 0:
        input("\nNo hay paises cargados, presiona Enter para volver al menu.. ")
        return
    print("\n///////////// PAISES /////////////\n")
    for pais in paises:
        print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")
    input("\nPresiona Enter para volver al menu.. ")

# Agregar pais
def agregar_pais():  # Agrego un pais nuevo verificando que no exista
    nombre = pedir_string("\nNombre del pais: ")
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            input(f"\nEl pais {nombre} ya existe, presiona Enter para volver al menu.. ")
            return
    poblacion = pedir_entero_positivo("Poblacion: ")
    superficie = pedir_entero_positivo("Superficie en km2: ")
    continente = pedir_string("Continente: ")
    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    input(f"\nEl pais {nombre} fue agregado correctamente! presiona Enter para volver al menu.. ")

# Actualizar pais
def actualizar_pais():  # Actualizo poblacion y superficie de un pais existente
    nombre = pedir_string("\nIngresa el nombre del pais que deseas actualizar: ")
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"\nDatos actuales de {pais['nombre']}:")
            print(f"Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2")
            pais["poblacion"] = pedir_entero_positivo("Nueva poblacion: ")
            pais["superficie"] = pedir_entero_positivo("Nueva superficie en km2: ")
            input(f"\nDatos de {pais['nombre']} actualizados correctamente! presiona Enter para volver al menu.. ")
            return
    input(f"\nEl pais {nombre} no existe, presiona Enter para volver al menu.. ")

# Buscar pais
def buscar_pais():  # Busco paises por coincidencia parcial o exacta en el nombre
    busqueda = pedir_string("\nIngresa el nombre o parte del nombre a buscar: ")
    resultados = []
    for pais in paises:
        if busqueda.lower() in pais["nombre"].lower():
            resultados.append(pais)
    if len(resultados) == 0:
        input(f"\nNo se encontraron paises con '{busqueda}', presiona Enter para volver al menu.. ")
        return
    print(f"\n/////// Resultados para '{busqueda}' ///////\n")
    for pais in resultados:
        print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")
    input("\nPresiona Enter para volver al menu.. ")

# Filtrar paises
def filtrar_paises():  # Submenu de filtros
    while True:
        try:
            opcion = int(input(
                "\n1. Por continente"
                "\n2. Por rango de poblacion"
                "\n3. Por rango de superficie"
                "\n4. Volver al menu principal"
                "\n\nElige una opcion: "
            ))
        except ValueError:
            input("\nError, asegurate de ingresar un valor numerico, presiona Enter para volver a intentarlo.. ")
        else:
            if opcion == 1:
                continente = pedir_string("\nIngresa el continente: ")
                resultados = []
                for pais in paises:
                    if pais["continente"].lower() == continente.lower():
                        resultados.append(pais)
                if len(resultados) == 0:
                    input(f"\nNo se encontraron paises en '{continente}', presiona Enter para volver al menu.. ")
                else:
                    print(f"\n/////// Paises en {continente} ///////\n")
                    for pais in resultados:
                        print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2")
                    input("\nPresiona Enter para volver al menu.. ")
            elif opcion == 2:
                min_pob = pedir_entero_positivo("\nPoblacion minima: ")
                max_pob = pedir_entero_positivo("Poblacion maxima: ")
                if min_pob > max_pob:
                    input("\nError, el minimo no puede ser mayor que el maximo, presiona Enter para volver al menu.. ")
                else:
                    resultados = []
                    for pais in paises:
                        if min_pob <= pais["poblacion"] <= max_pob:
                            resultados.append(pais)
                    if len(resultados) == 0:
                        input("\nNo se encontraron paises en ese rango de poblacion, presiona Enter para volver al menu.. ")
                    else:
                        print(f"\n/////// Paises con poblacion entre {min_pob} y {max_pob} ///////\n")
                        for pais in resultados:
                            print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")
                        input("\nPresiona Enter para volver al menu.. ")
            elif opcion == 3:
                min_sup = pedir_entero_positivo("\nSuperficie minima en km2: ")
                max_sup = pedir_entero_positivo("Superficie maxima en km2: ")
                if min_sup > max_sup:
                    input("\nError, el minimo no puede ser mayor que el maximo, presiona Enter para volver al menu.. ")
                else:
                    resultados = []
                    for pais in paises:
                        if min_sup <= pais["superficie"] <= max_sup:
                            resultados.append(pais)
                    if len(resultados) == 0:
                        input("\nNo se encontraron paises en ese rango de superficie, presiona Enter para volver al menu.. ")
                    else:
                        print(f"\n/////// Paises con superficie entre {min_sup} y {max_sup} km2 ///////\n")
                        for pais in resultados:
                            print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")
                        input("\nPresiona Enter para volver al menu.. ")
            elif opcion == 4:
                return
            else:
                input("\nError, solo puedes ingresar una opcion del 1 al 4, presiona Enter para volver a intentarlo.. ")

# Ordenar paises
def ordenar_paises():  # Submenu de ordenamiento
    while True:
        try:
            opcion = int(input(
                "\n1. Por nombre"
                "\n2. Por poblacion"
                "\n3. Por superficie"
                "\n4. Volver al menu principal"
                "\n\nElige una opcion: "
            ))
        except ValueError:
            input("\nError, asegurate de ingresar un valor numerico, presiona Enter para volver a intentarlo.. ")
        else:
            if opcion == 1:
                ordenados = sorted(paises, key=lambda p: p["nombre"].lower())
                print("\n/////// Paises ordenados por nombre ///////\n")
                for pais in ordenados:
                    print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")
                input("\nPresiona Enter para volver al menu.. ")
            elif opcion == 2 or opcion == 3:
                campo = "poblacion" if opcion == 2 else "superficie"
                while True:
                    try:
                        orden = int(input("\n1. Ascendente\n2. Descendente\n\nElige una opcion: "))
                    except ValueError:
                        input("\nError, asegurate de ingresar un valor numerico, presiona Enter para volver a intentarlo.. ")
                    else:
                        if orden == 1 or orden == 2:
                            descendente = orden == 2
                            ordenados = sorted(paises, key=lambda p: p[campo], reverse=descendente)
                            print(f"\n/////// Paises ordenados por {campo} ({'descendente' if descendente else 'ascendente'}) ///////\n")
                            for pais in ordenados:
                                print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")
                            input("\nPresiona Enter para volver al menu.. ")
                            break
                        else:
                            input("\nError, solo puedes ingresar 1 o 2, presiona Enter para volver a intentarlo.. ")
            elif opcion == 4:
                return
            else:
                input("\nError, solo puedes ingresar una opcion del 1 al 4, presiona Enter para volver a intentarlo.. ")

# Estadisticas
def estadisticas():  # Muestro estadisticas generales de los paises
    if len(paises) == 0:
        input("\nNo hay paises cargados, presiona Enter para volver al menu.. ")
        return

    mayor_pob = paises[0]
    menor_pob = paises[0]
    total_pob = 0
    total_sup = 0
    conteo_continentes = {}

    for pais in paises:
        if pais["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = pais
        if pais["poblacion"] < menor_pob["poblacion"]:
            menor_pob = pais
        total_pob = total_pob + pais["poblacion"]
        total_sup = total_sup + pais["superficie"]
        if pais["continente"] in conteo_continentes:
            conteo_continentes[pais["continente"]] = conteo_continentes[pais["continente"]] + 1
        else:
            conteo_continentes[pais["continente"]] = 1

    promedio_pob = total_pob / len(paises)
    promedio_sup = total_sup / len(paises)

    print("\n///////////// ESTADISTICAS /////////////\n")
    print(f"Pais con mayor poblacion: {mayor_pob['nombre']} ({mayor_pob['poblacion']})")
    print(f"Pais con menor poblacion: {menor_pob['nombre']} ({menor_pob['poblacion']})")
    print(f"Promedio de poblacion: {promedio_pob:.2f}")
    print(f"Promedio de superficie: {promedio_sup:.2f} km2")
    print("\nCantidad de paises por continente:")
    for continente in conteo_continentes:
        print(f"  {continente}: {conteo_continentes[continente]}")
    input("\nPresiona Enter para volver al menu.. ")

# Menu principal
def validacion_menu():  # Valido que el usuario ingrese una opcion valida
    while True:
        try:
            menu = int(input(
                "\n1. Agregar pais"
                "\n2. Actualizar pais"
                "\n3. Buscar pais"
                "\n4. Filtrar paises"
                "\n5. Ordenar paises"
                "\n6. Estadisticas"
                "\n7. Mostrar todos"
                "\n8. Salir"
                "\n\nElige una opcion: "
            ))
        except ValueError:
            input("\nError, solo puedes ingresar valores numericos, presiona Enter para volver a intentarlo.. ")
        else:
            if menu < 1 or menu > 8:
                input("\nError, solo puedes ingresar una opcion del 1 al 8, presiona Enter para volver a intentarlo.. ")
            else:
                return menu

# Inicio del programa
cargar_csv()

while True:
    menu = validacion_menu()
    if menu == 1:
        agregar_pais()
    elif menu == 2:
        actualizar_pais()
    elif menu == 3:
        buscar_pais()
    elif menu == 4:
        filtrar_paises()
    elif menu == 5:
        ordenar_paises()
    elif menu == 6:
        estadisticas()
    elif menu == 7:
        mostrar_todos()
    elif menu == 8:
        print("\nHasta luego!")
        break