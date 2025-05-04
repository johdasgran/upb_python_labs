# Laboratorio 4

# ['votó primer candidato', 'votó segundo candidato', 'votó en blanco']

# votos = [
#     [1, 0, 0],
#     [1, 0, 0],
#     [0, 0, 1]
# ]

votos = [
    [],
    [],
    []
]

def registro_votos(data):
    for i in range(len(data)):
        print(f'''
            Elección presidencial
                
            1. Candidato 1
            2. Candidato 2
            3. Voto en blanco 
            ''')
        opcion_selecionada = int(input("Selecione el candidado por el cual va a votar: "))
        if(opcion_selecionada >= 1 and opcion_selecionada <= 3):
            opcion_selecionada -= 1
            fila = [0, 0, 0]
            fila[opcion_selecionada] = 1
            votos[i] = fila
        else:
            print("Voto invalido")

registro_votos(votos)

# [id, nombre, canidad_de_votos, ganador, porcenaje_de_votos]
candidatos_por_votos = [
    [1, "Candidato 1", 0, False, 0],
    [2, "Candidato 2", 0, False, 0],
    [3, "Voto en blanco", 0, False, 0]
]

def tabulacion_votos(votos):
    for candidato in votos:
        index = 0
        for voto in candidato:
            if(voto):
                candidatos_por_votos[index][2] += 1
            index += 1

tabulacion_votos(votos)

candidatos_mas_votados = []

def calcular_ganador(candidatos):
    ganador = candidatos[0]
    for i in range (len(candidatos)):
        if(ganador[2] < candidatos[i][2]):
            ganador = candidatos[i]
        
    for i in range (len(candidatos)):
        if(candidatos[i][2] == ganador[2]):
            candidatos_mas_votados.append(candidatos[i])
            candidatos_por_votos[i][3] = True

calcular_ganador(candidatos_por_votos)

def visualizar_resultados(candidatos):
    for i in range (len(candidatos)):
        candidatos_por_votos[i][4] = format(candidatos_por_votos[i][2]/(len(votos))*100, ".2f")
        print(f"{candidatos_por_votos[i][0]}. {candidatos_por_votos[i][1]} con {candidatos_por_votos[i][2]} votos y un porcentaje de {candidatos_por_votos[i][4]}%")

    if(len(candidatos_mas_votados) == 1 and candidatos_mas_votados[0][0] != 3):
        print(f"El ganador es: {candidatos_mas_votados[0][1]} con {candidatos_mas_votados[0][2]} votos y el {candidatos_mas_votados[0][4]}% de los votos")
    else:
        print("No hay ganador claro, se require de segunda vuelta")

visualizar_resultados(candidatos_por_votos)