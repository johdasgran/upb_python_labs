equipos = [
    [1, "Bucaramanga", 0],
    [2, "Universitario", 0],
    [3, "Barcelona", 0],
    [4, "Fortaleza", 0],
    [5, "Olimpia", 0],
    [6, "Peñarol", 0],
    [7, "Universidad de Chile", 0],
    [8, "Bolívar", 0],
    [9, "Palmiras", 0],
    [10, "Carabobo", 0],
    [11, "Alianza Lima", 0],
    [12, "Nacional", 0]
]

tabla_posiciones = []

# PG = 3
# PE = 1
# PP = 0

equipos_divididos = int(len(equipos)/2)
equipos_temp = equipos.copy()
equipos_ya_jugaron = []


for i in range(equipos_divididos):
    print("Equipos de juegos")

    for equipo in equipos_temp:
        if(equipo not in equipos_ya_jugaron):
            print(f"{equipo[0]}. {equipo[1]}")

    equipo_1 = int(input("Selecione el numero(id) del equipo 1: "))
    equipo_2 = int(input("Selecione el numero(id) del equipo 2: "))
    goles_equipo_1 = int(input("Selecione los goles del equipo 1: "))
    goles_equipo_2 = int(input("Selecione los goles del equipo 2: "))

    if(goles_equipo_1 > goles_equipo_2):
        equipo_ganador_1 = equipos[equipo_1-1]
        equipo_ganador_2 = equipos[equipo_2-1]
        equipo_ganador_1[2] += 3
        equipo_ganador_2[2] += 0

    if(goles_equipo_1 < goles_equipo_2):
        equipo_ganador_1 = equipos[equipo_1-1]
        equipo_ganador_2 = equipos[equipo_2-1]
        equipo_ganador_1[2] += 0
        equipo_ganador_2[2] += 3

    if(goles_equipo_1 == goles_equipo_2): 
        equipo_ganador_1 = equipos[equipo_1-1]
        equipo_ganador_2 = equipos[equipo_2-1]

        equipo_ganador_1[2] += 1
        equipo_ganador_2[2] += 1

    tabla_posiciones.append(equipo_ganador_1)
    tabla_posiciones.append(equipo_ganador_2)

    equipos_ya_jugaron.append(equipo_ganador_1)
    equipos_ya_jugaron.append(equipo_ganador_2)

tabla_posiciones_temp = tabla_posiciones.copy()
tabla_posiciones_by_puntos = []

def order_by_puntos(list):
    id = list[0][2]
    for i in range(len(list)):
        if(id < list[i][2]):
            id = list[i][2]
    return id

while tabla_posiciones_temp:
    mayor = order_by_puntos(tabla_posiciones_temp)
    for equipo in tabla_posiciones_temp:
        if equipo[2] == mayor:
            tabla_posiciones_by_puntos.append(equipo)
            tabla_posiciones_temp.remove(equipo)
            break


print("Tabla de posiciones final")
for equipo in tabla_posiciones_by_puntos:
    print(f"{equipo[0]}. {equipo[1]} - Puntos: {equipo[2]}")


# No me acuerdo si tocaba hacer las vueltas que
# seguian pero creo que solo era las posiciones de 
# la primera vuelta xd