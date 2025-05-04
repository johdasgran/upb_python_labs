# Metrolinea lab

while True:
    cantidad_total_viajes = int(input("Ingrese la cantidad de viajes: "))
    if(cantidad_total_viajes < 0):
        print("Debe ser un numero positivo")
    if(cantidad_total_viajes >= 0):
        break

while True:
    saldo_actual = int(input("Ingrese el saldo actual (sin puntos o comas): "))
    if(saldo_actual < 0):
        print("Debe ser un numero positivo")
    if(saldo_actual >= 0):
        break

while True:
    print(f'''
        Tipo de usuario
            
        1. Estudiante
        2. Adulto Mayor
        3. General 
        ''')
    tipo_usuario = int(input("Ingrese el tipo de usuario: "))
    if(tipo_usuario < 1 or tipo_usuario > 3):
        print("Debe ingresar una opcion valida")
    if(tipo_usuario >= 1 and tipo_usuario <= 3):
        break

while True:
    transbordo = int(input("Ingrese el 1 si hay transbordo o 0 si no lo hay: "))
    if(transbordo == 1 or transbordo == 0): 
        if(transbordo == 1):
            transbordo = True
            while True:
                viajes_con_transbordo = int(input("Ingrese la cantidad de viajes con transbordo: "))
                if(viajes_con_transbordo < 0):
                    print("Debe ser un numero positivo")
                if(viajes_con_transbordo > 0):
                    break
            break
        if(transbordo == 0):
            transbordo = False
            viajes_con_transbordo = 0
            break
    print("Debe selecionar una opción valida 1 si hay y 0 si no lo hay")

dias_de_la_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

while True:
    for i in range(len(dias_de_la_semana)):
        print(f"{i+1}. {dias_de_la_semana[i]}")
    
    dia = int(input("Ingrese el dia de la semana (numero): "))
    if(dia < 1 or dia > 7):
        print("Debe ingresar una opción valida")
    if(dia >= 1 and dia <= 7):
        dia -= 1
        for d in range (len(dias_de_la_semana)):
            if(d == dia):
                dia = dias_de_la_semana[d].lower()
        break


params = {
    'cantidad_total_viajes': cantidad_total_viajes,
    'saldo_actual': saldo_actual,
    'tipo_usuario': tipo_usuario,
    'transbordo': transbordo,
    'viajes_con_transbordo': viajes_con_transbordo,
    'dia': dia
}

valor_pasaje_base = 3200

# despues del 3 se cuenta como viaje adicional

def metrolinea(params, valor_pasaje_base):
    saldo_requerido = 0
    descuento = 0
    for i in range(params['cantidad_total_viajes']):
        if(params['tipo_usuario'] == 1):
           descuento = 20
        if(params['tipo_usuario'] == 2):
           descuento = 50
        if(params['tipo_usuario'] == 3):
           descuento = 0
        if(params['dia'].lower() == 'miercoles'):
            descuento += 10
        if(descuento != 0):
            saldo_requerido += valor_pasaje_base - (valor_pasaje_base * descuento)/100
        else:
            saldo_requerido += valor_pasaje_base

    for i in range(params['viajes_con_transbordo']):
        if(i == 0):
            saldo_requerido += 500
        if(i == 1):
            saldo_requerido += 300
        if(i >= 2):
            saldo_requerido += valor_pasaje_base - (valor_pasaje_base * descuento)/100


    if(params['dia'].lower() == 'miercoles'):
        print("Hoy es Miercoles y hay una promocion de 10% de descuento")
    if(saldo_requerido > params['saldo_actual']):
        print(f"El costo total de los viajes es {saldo_requerido}$")
        print(f"El saldo actual es: {params['saldo_actual']}$")
        print(f"El saldo que falta por recargar es: {saldo_requerido - params['saldo_actual']}$")
        if(params['transbordo']):
            print(f"Hay {params['viajes_con_transbordo']} con transbordo")
            print("El primero tiene un valor de 500$")
            print("El segundo tiene un valor de 300$")
            print(f"A partir del tercero se cobra como pasaje adicional y tiene un precio de {valor_pasaje_base}$ c/u y con un descuento de {descuento}% y es igual a {valor_pasaje_base - (valor_pasaje_base * descuento)/100}$ cada pasaje")
    else:
        print("No se necesita recargar, ya se tiene suficiente en la tarjeta")
        print(f"Saldo requerido: {saldo_requerido}$")
        print(f"Saldo actual: {params['saldo_actual']}$")


metrolinea(params, valor_pasaje_base)