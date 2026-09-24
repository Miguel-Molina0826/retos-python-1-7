notas = (4.5,4.7,3.5,2.6,4.5)

promedio = sum(notas) / len(notas)
print(promedio)



dias_semana = dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

print(dias_semana[0])
print(dias_semana[-1])
print(dias_semana[5:])


asistencia = [False] * 10
print ("marcador inicial", asistencia)
print("longitud de la lista",len(asistencia))


palabra  = input("ingrese una palabra")

palabra_mitad = len(palabra) // 2

print("lista de letras",palabra)
print("mitad de la palabra",palabra_mitad)


notass = (4.5,4.7,3.5,2.6,4.5)
indice = int(input("ingrese el índice que quieres buscar"))

if indice < len(notas):
    print ("el valor en esta pocision es", notass[indice])
else:
    print("el indice esta fura de rango ")



notas = [3.5, 4.8, 2.9, 5.0, 4.1]


if notas[0] > notas[1]:
    notas[0], notas[1] = notas[1], notas[0]
if notas[1] > notas[2]:
    notas[1], notas[2] = notas[2], notas[1]
if notas[2] > notas[3]:
    notas[2], notas[3] = notas[3], notas[2]
if notas[3] > notas[4]:
    notas[3], notas[4] = notas[4], notas[3]

# Pasada 2
if notas[0] > notas[1]:
    notas[0], notas[1] = notas[1], notas[0]
if notas[1] > notas[2]:
    notas[1], notas[2] = notas[2], notas[1]
if notas[2] > notas[3]:
    notas[2], notas[3] = notas[3], notas[2]

# Pasada 3
if notas[0] > notas[1]:
    notas[0], notas[1] = notas[1], notas[0]
if notas[1] > notas[2]:
    notas[1], notas[2] = notas[2], notas[1]

# Pasada 4
if notas[0] > notas[1]:
    notas[0], notas[1] = notas[1], notas[0]


tres_mas_altas = notas[2:]


print("Lista ordenada manualmente:", notas)
print("Las tres notas más altas son:", tres_mas_altas)










