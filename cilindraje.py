cilindrajes = []
suma_cilindrajes = 0
cilindrajes_menores_promedio = []

cantidad_cilidrajes = int(input("Ingrese la cantidad de cilidrajes que se van a ingresar: "))

for i in range (0, cantidad_cilidrajes):
    cilindraje = int(input("Ingrese el cilindraje: "))
    cilindrajes.append(cilindraje)
    suma_cilindrajes += cilindraje

promedio_cilindrajes = suma_cilindrajes/len(cilindrajes)

for cilindraje in cilindrajes:
    if(cilindraje < promedio_cilindrajes):
        cilindrajes_menores_promedio.append(cilindraje)

print(f"El promedio de los cilidrajes ingresados es: {promedio_cilindrajes}")
print(f"Los cilidrajes menores al promedio son: {cilindrajes_menores_promedio}")
