
temperaturas = [18, -4, 25, 12, -2, 30, 5, -8]

# A mano con patrones
max_mano = temperaturas[0]
min_mano = temperaturas[0]
suma = 0
cantidad = 0

for t in temperaturas:
    if t > max_mano:
        max_mano = t
    if t < min_mano:
        min_mano = t
    suma += t
    cantidad += 1

promedio_mano = suma / cantidad
print(f"[A mano] Máxima: {max_mano}, Mínima: {min_mano}, Promedio: {promedio_mano}")

# Con funciones integradas
print(f"[Integradas] Máxima: {max(temperaturas)}, Mínima: {min(temperaturas)}, Promedio: {sum(temperaturas)/len(temperaturas)}")


palabras = ["python", "sol", "programacion", "git", "computadora"]
contador = 1

print("\n--- Palabras con más de 5 letras ---")
for p in palabras:
    if len(p) > 5:
        print(f"{contador}. {p}")
        contador += 1



precios = [10000, 25500, 4800, 120000]
precios_con_iva = []

for precio in precios:
    iva = precio * 1.19
    precios_con_iva.append(round(iva, 2))

print("\nPrecios originales:", precios)
print("Precios con IVA (19%):", precios_con_iva)



nombres = ["Carlos", "Sofía", "Mateo", "Lucía", "Ana"]
iniciales = []

for nombre in nombres:
    iniciales.append(nombre[0])

print("\nNombres:", nombres)
print("Iniciales:", iniciales)



calificaciones = [4.5, 3.2, 4.8, 2.0, 3.9]
aprobadas_mal = []

for nota in calificaciones:
    aprobadas_mal = [] # BUG: Al estar dentro, la lista se borra en cada iteración
    if nota >= 3.0:
        aprobadas_mal.append(nota)

print("\n[Rómpelo] Resultado con el bug (solo guarda la última si pasa):", aprobadas_mal)



lista_original = [3, 5, 2, 5, 8, 3, 9, 2, 3]
duplicados_multiples = []
ya_avisados = []

for elemento in lista_original:
    if lista_original.count(elemento) > 1:
        if elemento not in ya_avisados:
            duplicados_multiples.append(elemento)
            ya_avisados.append(elemento)

print("\n--- NIVEL JEFE ---")
print("Lista original:", lista_original)
print("Valores que aparecen más de una vez (sin repetir aviso):", duplicados_multiples)