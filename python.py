# listado quemado para pruebas he he 👾

# vacas_hembras = [
#     [282, 'Vaca'],
#     [444, 'Vaca'],
#     [888, 'Vaca'],
#     [224, 'Vaca'],
#     [666, 'Vaca']
# ]

# vacas_machos = [
#     [153, 'Vaca'],
#     [793, 'Vaca'],
#     [133, 'Vaca'],
#     [993, 'Vaca'],
#     [111, 'Vaca']
# ]

vacas_hembras = []
vacas_machos = []

# id hembras numeros pares
# id machos numeros impares

while True:
    vaca_id = int(input("Ingrese el id (deben ser 3 digitos) de la vaca: "))

    if(len(str(vaca_id)) < 3 or len(str(vaca_id)) > 3):
        while len(str(vaca_id)) < 3 or len(str(vaca_id)) > 3:
            print("El id debe ser de 3 digitos! vuelve a intentar...")
            vaca_id = int(input("Ingrese el id (deben ser 3 digitos) de la vaca: "))


    vaca_name = input("Ingrese el nombre de la vaca: ")
    print("Agregando al potrero...")

    if(vaca_id % 2 == 0):
        vacas_hembras.append([vaca_id, vaca_name])
    else:
        vacas_machos.append([vaca_id, vaca_name])

    print("Vaca agregada")

    option = input("¿Quieres agregar más vacas? escribe 'si' o 'fin' para salir: ")
    if(option.lower() == 'fin'):
        break


# list ASC or DESC
# ASC = Mayor a menor
# DESC = menor a mayor

# machos mayor a menor
# hembras menor a mayor

vacas_machos_ordenados = []
vacas_hembras_ordenados = []


def order(list, order):
    id = list[0][0]

    if(order.upper() == 'ASC'):
        for i in range(len(list)):
            if(id < list[i][0]):
                id = list[i][0]

    if(order.upper() == 'DESC'):
        for i in range(len(list)):
            if(id > list[i][0]):
                id = list[i][0]

    return id


vacas_machos_temp = vacas_machos.copy()
vacas_hembras_temp = vacas_hembras.copy()

while vacas_machos_temp:
    id_mayor = order(vacas_machos_temp, 'ASC')
    for vaca in vacas_machos_temp:
        if vaca[0] == id_mayor:
            vacas_machos_ordenados.append(vaca)
            vacas_machos_temp.remove(vaca)
            break

while vacas_hembras_temp:
    id_menor = order(vacas_hembras_temp, 'DESC')
    for vaca in vacas_hembras_temp:
        if vaca[0] == id_menor:
            vacas_hembras_ordenados.append(vaca)
            vacas_hembras_temp.remove(vaca)
            break


print("Vacas machos (ceba) ordenados ASC", vacas_machos_ordenados)
print("Vacas hembras (leche) ordenados DESC", vacas_hembras_ordenados)
