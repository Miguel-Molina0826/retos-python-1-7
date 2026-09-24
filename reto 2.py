fila = ["juan","carlos","ana","lina","miguel"]
while len(fila)>0:
     atendido = fila.pop(0)
     quedan = len(fila)

     print(f"atendiendoa{atendido}.quedan{quedan} en la fila")

print("fial vacia todos han sido atendidos")


numeros = [0]
for i in range(5):
    valor=float (input(f"ingresa el numero {i+1}:"))
    numeros.append(valor)
numeros.sort(reverse=True)

print("lista ordenada",numeros)
print("el top 3 numeros mas altos es:", numeros[:3])


lista_original = [2,3,5,5,3,2,7,1,8,9,9,8,7,2]

unicos = []
for numero in lista_original:
     if lista_original.count(numero) ==1:
        unicos.append(numero)

print("lista original", lista_original)
print("valores que aparecen una sola vez", unicos)


historial = []

historial.append("como programar en python")
historial.append("youtube")
historial.append("como insertar una imagen en word")

print("historial actual:", historial)

respuesta = input("¿Quieres deshacer la última búsqueda? ('si' o 'no'): ")

if respuesta.lower() == "si":
    if len(historial) > 0:
        accion_deshecha = historial.pop()
        print(f"'{accion_deshecha}' se eliminó")
    else:
        print("el historial está vacío")
else:
    print("no se ha modificado el historial")

print("historial actualizado:", historial)



lista = [5, 2, 9, 1]

lista.sort()

print("Lista ordenada correctamente:", lista)




nombres = ["Carlos", "Sofía", "Mateo", "Lucía", "Ana"]
puntajes = [85, 98, 72, 91, 65]


if puntajes[0] < puntajes[1]:
    puntajes[0], puntajes[1] = puntajes[1], puntajes[0]
    nombres[0], nombres[1] = nombres[1], nombres[0]

if puntajes[1] < puntajes[2]:
    puntajes[1], puntajes[2] = puntajes[2], puntajes[1]
    nombres[1], nombres[2] = nombres[2], nombres[1]

if puntajes[2] < puntajes[3]:
    puntajes[2], puntajes[3] = puntajes[3], puntajes[2]
    nombres[2], nombres[3] = nombres[3], nombres[2]

if puntajes[3] < puntajes[4]:
    puntajes[3], puntajes[4] = puntajes[4], puntajes[3]
    nombres[3], nombres[4] = nombres[4], nombres[3]


if puntajes[0] < puntajes[1]:
    puntajes[0], puntajes[1] = puntajes[1], puntajes[0]
    nombres[0], nombres[1] = nombres[1], nombres[0]

if puntajes[1] < puntajes[2]:
    puntajes[1], puntajes[2] = puntajes[2], puntajes[1]
    nombres[1], nombres[2] = nombres[2], nombres[1]

if puntajes[2] < puntajes[3]:
    puntajes[2], puntajes[3] = puntajes[3], puntajes[2]
    nombres[2], nombres[3] = nombres[3], nombres[2]


if puntajes[0] < puntajes[1]:
    puntajes[0], puntajes[1] = puntajes[1], puntajes[0]
    nombres[0], nombres[1] = nombres[1], nombres[0]

if puntajes[1] < puntajes[2]:
    puntajes[1], puntajes[2] = puntajes[2], puntajes[1]
    nombres[1], nombres[2] = nombres[2], nombres[1]


if puntajes[0] < puntajes[1]:
    puntajes[0], puntajes[1] = puntajes[1], puntajes[0]
    nombres[0], nombres[1] = nombres[1], nombres[0]


print("--- PODIO DE GANADORES ---")
print(f"1. {nombres[0]} con {puntajes[0]} puntos")
print(f"2. {nombres[1]} con {puntajes[1]} puntos")
print(f"3. {nombres[2]} con {puntajes[2]} puntos")
