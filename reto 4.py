
DIAS = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

print("--- 1. Día de la semana ---")
numero = int(input("Ingresa un número del 1 al 7: "))
if 1 <= numero <= 7:
    # Restamos 1 porque los índices de las tuplas comienzan en 0
    print(f"El día correspondiente es: {DIAS[numero - 1]}")
else:
    print("Error: El número debe estar estrictamente entre 1 y 7.")



ciudades_coordenadas = [
    ("Bogotá", 4.6097, -74.0817),
    ("Medellín", 6.2442, -75.5812),
    ("Cali", 3.4516, -76.5320),
    ("Barranquilla", 10.9685, -74.7813),
    ("Cartagena", 10.3910, -75.4794)
]

print("\n--- 2. Ciudades y coordenadas alineadas ---")
print(f"{'Ciudad':<15} | {'Latitud':<10} | {'Longitud':<10}")
print("-" * 43)
for ciudad, lat, lon in ciudades_coordenadas:
    print(f"{ciudad:<15} | {lat:<10} | {lon:<10}")



print("\n--- 3. Intercambio de variables ---")
a = 10
b = 20
print(f"Antes: a = {a}, b = {b}")

a, b = b, a

print(f"Después: a = {a}, b = {b}")



print("\n--- 4. Orden alfabético con sorted() ---")
ciudades_ordenadas = sorted(ciudades_coordenadas)
for c in ciudades_ordenadas:
    print(c)
# Explicación: sorted() ordena por defecto tomando el primer elemento de la tupla (la ciudad).
# Tiene sentido porque compara las cadenas de texto alfabéticamente de la A a la Z.





print("\n--- NIVEL JEFE: Podio por puntaje ---")
competidores = [("Carlos", 85), ("Sofía", 98), ("Mateo", 72), ("Lucía", 91), ("Ana", 65)]


podio = sorted(competidores, key=lambda x: x[1], reverse=True)

print("Los 3 primeros puestos:")
for i in range(3):
    nombre, puntaje = podio[i]
    print(f"{i + 1}. {nombre} con {puntaje} puntos")