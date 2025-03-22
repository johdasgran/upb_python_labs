def init_lab():
    print("** Welcome to Python labs ** /n")
    print("1. Calcular el area de un triangulo /n")
    print("2. Calcular días del mes /n")
    print("3. Calcular el mayor de 10 numeros /n")
    print("4. Calcular la tabla de potencias del 1 al 10 de un numero /n")
    print("5. Validar palindromo")
    print("6. Suma de numeros por lista /n")
    print("7. Salir del lab /n")

    option = int(input("Selecione la opción que desea probar :) "))
    if(option==1):
        area_triangulo()
    elif(option==2):
        dias_mes()
    elif(option==3):
        buscar_mayor()
    elif(option==4):
        potencia()
    elif(option==5):
        es_palindromo()
    elif(option==6):
        suma_numeros()
    else:
        print("Selecion invalida")


def area_triangulo():
    base = int(input("Ingrese la base del triangulo: "))
    altura = int(input("Ingrese la altura del triangulo: "))
    area = base*altura
    print(f"El area del triangulo es: {area}")

def dias_mes():
    day = int(input("Ingrese el numero del mes: "))
    day = day - 1
    year = int(input("Ingrese el año: "))
    daysPerYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    namePerMonth = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        # Es bisiesto
        daysPerYear[1] = 29
    print(f"Los días {namePerMonth[day]} en el año {year} son: {daysPerYear[day]}")

def buscar_mayor(): 
    count = 0
    listNumeros = []
    for count in range(0, 10):
        count = count + 1
        numero = int(input(f"Ingrese el numero {count}: "))
        listNumeros.append(numero)
    numero_mayor = sorted(listNumeros, reverse=True)[0]
    print(f"El numero mayor es: {numero_mayor}")

def potencia():
    numero = int(input("Ingrese un numero: "))
    count = 0
    for count in range(0, 10):
        count = count + 1
        print(f"Potencia de {numero} a la {count}: {numero**count}")

def es_palindromo(): 
    palabra = str(input("Ingrese una palabra"))
    if(palabra == palabra[::-1]):
        print("True")
    print("False")

def suma_numeros():
    suma = []


init_lab()