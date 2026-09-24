
productos = ["Manzanas", "Peras", "Bananos", "Naranjas"]
cantidades = [25, 40, 15, 30]


inventario = dict(zip(productos, cantidades))

print("--- 1. Inventario Completo ---")
print(f"{'Producto':<15} | {'Cantidad':<10}")
print("-" * 30)
total_inventario = 0

for producto, cantidad in inventario.items():
    print(f"{producto:<15} | {cantidad:<10}")
    total_inventario += cantidad

print("-" * 30)
print(f"Total de elementos en el inventario: {total_inventario}")



print("\n--- 2. Contador de palabras ---")
frase = input("Ingresa una frase: ")
palabras = frase.split()
contador_palabras = {}

for palabra in palabras:
    contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, veces in contador_palabras.items():
    print(f"'{palabra}': {veces} vez/veces")


print("\n--- 3. Traductor Español -> Inglés ---")
traductor = {
    "perro": "dog",
    "gato": "cat",
    "casa": "house",
    "carro": "car",
    "agua": "water",
    "sol": "sun",
    "luna": "moon",
    "libro": "book",
    "manzana": "apple",
    "computadora": "computer"
}

palabra_esp = input("Ingresa una palabra en español para traducir: ").lower()
traduccion = traductor.get(palabra_esp)

if traduccion:
    print(f"Traducción: {traduccion}")
else:
    print("La palabra no está en el diccionario.")
    agregar = input("¿Deseas agregarla? (s/n): ")
    if agregar.lower() == 's':
        nueva_trad = input(f"Ingresa la traducción en inglés de '{palabra_esp}': ")
        traductor[palabra_esp] = nueva_trad
        print("¡Palabra agregada con éxito!")


print("\n--- 4. Conteo de votos de una encuesta ---")
votos = ["azul", "rojo", "azul", "verde", "azul"]
conteo_votos = {}

for voto in votos:
    conteo_votos[voto] = conteo_votos.get(voto, 0) + 1


campeon = None
max_votos = -1

for opcion, cantidad in conteo_votos.items():
    if cantidad > max_votos:
        max_votos = cantidad
        campeon = opcion

print(f"Los votos fueron: {votos}")
print(f"El ganador de la encuesta es '{campeon}' con {max_votos} votos.")




print("\n--- NIVEL JEFE: Histograma de Frecuencia de Letras ---")
texto = "escribe un contador de letras que ademas muestre la letra mas frecuente"

# Limpiamos el texto de espacios para contar solo letras
texto_limpio = texto.replace(" ", "")
conteo_letras = {}

for letra in texto_limpio:
    conteo_letras[letra] = conteo_letras.get(letra, 0) + 1

letras_ordenadas = sorted(conteo_letras.items(), key=lambda x: x[1], reverse=True)

print(f"Texto analizado: '{texto}'\n")
print(f"{'Letra':<6} | {'Veces':<6} | Histograma")
print("-" * 35)

for letra, veces in letras_ordenadas:
    print(f"{letra:<6} | {veces:<6} | {'#' * veces}")


letra_mas_frecuente, max_freq = letras_ordenadas[0]
print("-" * 35)
print(f"La letra más frecuente es '{letra_mas_frecuente}' con {max_freq} apariciones.")
