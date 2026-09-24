
print("--- 1. Tablero de Tres en Raya ---")

tablero = [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(t):
    print("  0   1   2")
    for idx, fila in enumerate(t):
        print(f"{idx} " + " | ".join(fila))
        if idx < 2:
            print(" ---+---+---")

mostrar_tablero(tablero)


fila = int(input("Elige fila (0-2): "))
columna = int(input("Elige columna (0-2): "))

if 0 <= fila <= 2 and 0 <= columna <= 2:
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = "X"
        print("¡Casilla marcada con éxito!")
        mostrar_tablero(tablero)
    else:
        print("La casilla ya está ocupada.")
else:
    print("Coordenadas fuera de rango (debe ser de 0 a 2).")


print("\n--- 2. Lista de diccionarios (Podio) ---")
competidores_dict = [
    {"nombre": "Carlos", "puntaje": 85},
    {"nombre": "Sofía", "puntaje": 98},
    {"nombre": "Mateo", "puntaje": 72},
    {"nombre": "Lucía", "puntaje": 91},
    {"nombre": "Ana", "puntaje": 65}
]

podio_dict = sorted(competidores_dict, key=lambda x: x["puntaje"], reverse=True)

print("Podio usando diccionarios:")
for i in range(3):
    print(f"{i + 1}. {podio_dict[i]['nombre']} con {podio_dict[i]['puntaje']} puntos")


print("\n--- 3. Inventario de tienda ---")
inventario_tienda = [
    {"nombre": "Camisa", "precio": 45000, "cantidad": 12},
    {"nombre": "Pantalón", "precio": 80000, "cantidad": 3},
    {"nombre": "Zapatos", "precio": 120000, "cantidad": 4},
    {"nombre": "Gorras", "precio": 25000, "cantidad": 20}
]

valor_total = 0
bajas_unidades = []

for item in inventario_tienda:
    valor_total += item["precio"] * item["cantidad"]
    if item["cantidad"] < 5:
        bajas_unidades.append(item["nombre"])

print(f"Valor total del inventario: ${valor_total}")
print(f"Productos con menos de 5 unidades: {bajas_unidades}")



print("\n--- 4. Copia superficial vs Profunda ---")
import copy

datos = [{"id": 1, "config": {"tema": "oscuro"}}]


respaldo = datos.copy()
respaldo[0]["config"]["tema"] = "claro"
print("Al modificar el respaldo superficial, ¡el original también cambió por referencia interna!")
print("Valor en original:", datos[0]["config"]["tema"])

datos_reales = [{"id": 1, "config": {"tema": "oscuro"}}]
respaldo_seguro = copy.deepcopy(datos_reales)
respaldo_seguro[0]["config"]["tema"] = "claro"

print("\nUsando copy.deepcopy():")
print("Original intacto:", datos_reales[0]["config"]["tema"])
print("Respaldo modificado:", respaldo_seguro[0]["config"]["tema"])


print("\n--- NIVEL JEFE: Diccionario de listas y Promedios ---")
estudiantes = [
    {"nombre": "Carlos", "grupo": "A", "puntaje": 85},
    {"nombre": "Sofía", "grupo": "B", "puntaje": 98},
    {"nombre": "Mateo", "grupo": "A", "puntaje": 72},
    {"nombre": "Lucía", "grupo": "C", "puntaje": 91},
    {"nombre": "Ana", "grupo": "B", "puntaje": 65},
    {"nombre": "Pedro", "grupo": "C", "puntaje": 80}
]

grupos = {}

for alumno in estudiantes:
    clave = alumno["grupo"]

    grupos.setdefault(clave, []).append(alumno)

print("Promedio de puntajes por cada grupo:")
for grupo, miembros in grupos.items():
    suma_puntajes = sum(m["puntaje"] for m in miembros)
    promedio = suma_puntajes / len(miembros)
    print(f"Grupo {grupo}: Promedio de {promedio:.2f} puntos")
