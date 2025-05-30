cambios_diarios = [1, 2, 3, 7, 5]
objetivo = 15
exist = False
suma_acumulada = 0
suma_vistas = {0: True}

for num in cambios_diarios:
    suma_acumulada += num
    if (suma_acumulada - objetivo) in suma_vistas:
        exist = True
    suma_vistas[suma_acumulada] = True

if(exist):
    print("Si existe un subarreglo con suma objetivo")
else:
    print("No existe un subarreglo con suma objetivo")-