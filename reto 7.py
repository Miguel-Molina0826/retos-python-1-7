
biblioteca = [
    {"titulo": "Cien años de soledad", "paginas": 417, "leido": True},
    {"titulo": "El Principito", "paginas": 96, "leido": True},
    {"titulo": "1984", "paginas": 328, "leido": False},
    {"titulo": "Fahrenheit 451", "paginas": 158, "leido": False}
]

while True:
    print("\n--- GESTOR DE BIBLIOTECA ---")
    print("1. Ver catálogo completo")
    print("2. Agregar nuevo libro (con validación de duplicados)")
    print("3. Marcar libro como leído")
    print("7. Ver pendientes (ordenados de menor a mayor página)")
    print("8. Eliminar libro del catálogo")
    print("9. Salir")

    opcion = input("Elige una opción (1-9): ")

    if opcion == "1":
        print("\n--- CATÁLOGO COMPLETO ---")
        if not biblioteca:
            print("La biblioteca está vacía.")
        else:
            print(f"{'No.':<4} | {'Título':<25} | {'Páginas':<8} | {'Leído'}")
            print("-" * 50)
            for idx, libro in enumerate(biblioteca, 1):
                estado = "Sí" if libro["leido"] else "No"
                print(f"{idx:<4} | {libro['titulo']:<25} | {libro['paginas']:<8} | {estado}")

    elif opcion == "2":
        print("\n--- AGREGAR LIBRO ---")
        nuevo_titulo = input("Título del libro: ").strip()


        duplicado = False
        for libro in biblioteca:
            if libro["titulo"].lower() == nuevo_titulo.lower():
                duplicado = True
                break

        if duplicado:
            print("❌ Error: ¡Ese libro ya existe en el catálogo y no se permiten duplicados!")
        else:
            try:
                paginas = int(input("Número de páginas: "))
                leido_input = input("¿Ya lo leíste? (s/n): ").lower()
                leido = True if leido_input == 's' else False

                biblioteca.append({"titulo": nuevo_titulo, "paginas": paginas, "leido": leido})
                print("✅ ¡Libro agregado con éxito al catálogo!")
            except ValueError:
                print("❌ Error: El número de páginas debe ser un valor numérico entero.")

    elif opcion == "3":
        print("\n--- MARCAR LIBRO COMO LEÍDO ---")
        if not biblioteca:
            print("No hay libros registrados.")
        else:
            for idx, libro in enumerate(biblioteca, 1):
                estado = "Leído" if libro["leido"] else "Pendiente"
                print(f"{idx}. {libro['titulo']} [{estado}]")
            try:
                num = int(input("Ingresa el número del libro que terminaste de leer: "))
                if 1 <= num <= len(biblioteca):
                    biblioteca[num - 1]["leido"] = True
                    print(f"🎉 ¡'{biblioteca[num - 1]['titulo']}' marcado como leído!")
                else:
                    print("❌ Error: El número está fuera del rango del catálogo.")
            except ValueError:
                print("❌ Por favor ingresa un número válido.")

    elif opcion == "7":
        print("\n--- 7. LIBROS PENDIENTES (Ordenados por menor extensión) ---")

        pendientes = [l for l in biblioteca if not l["leido"]]

        if not pendientes:
            print("¡Excelente trabajo! No tienes libros pendientes por leer.")
        else:

            pendientes_ordenados = sorted(pendientes, key=lambda x: x["paginas"])

            print(f"{'Título':<25} | {'Páginas':<8}")
            print("-" * 37)
            for libro in pendientes_ordenados:
                print(f"{libro['titulo']:<25} | {libro['paginas']:<8}")

    elif opcion == "8":
        print("\n--- 8. ELIMINAR LIBRO ---")
        if not biblioteca:
            print("El catálogo está vacío, no hay nada que eliminar.")
        else:
            for idx, libro in enumerate(biblioteca, 1):
                print(f"{idx}. {libro['titulo']}")
            try:
                num = int(input("Ingresa el número exacto del catálogo que deseas eliminar: "))
                if 1 <= num <= len(biblioteca):

                    libro_retirado = biblioteca.pop(num - 1)
                    print(f"🗑️ Se ha retirado con éxito del catálogo: '{libro_retirado['titulo']}'")
                else:
                    print("❌ Error: El número ingresado no existe en el catálogo.")
            except ValueError:
                print("❌ Entrada inválida. Debes ingresar un número entero.")

    elif opcion == "9":
        print("¡Saliendo del programa. Buen trabajo con tus colecciones!")
        break
    else:
        print("❌ Opción no válida. Por favor selecciona un número del menú entre 1 y 9.")