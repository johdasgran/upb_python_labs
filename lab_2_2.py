# Laboratorio 2 - Segundo Corte

# Calcular el factorial de un numero entero positivo 

numero = int(input("Ingrese un numero (Factorial): "))
factorial = 0

while(numero < 0):
    print("El numero debe ser positivo")
    numero = int(input("Ingrese un numero (Factorial)): "))

# index = numero
# for i in range(0, numero):
#     indexTemp = index
#     index = index - 1
#     if(i == 0):
#         factorial = index*indexTemp
#     if(index > 0 and i != 0):
#         factorial = factorial*index
#         print(f"factorial {factorial}")

# fancy way xd range(start, stop, step)

for i in range(numero, 0, -1):
    i_temp = i-1
    if(i == numero):
        factorial = i*i_temp
    if(i != numero and i_temp != 0):
        factorial = factorial*i_temp

print(f"El factorial es: {factorial}")


# Imprimir los primeros n numeros de la serie Fibonacci
numero = int(input("Ingrese un numero (Fibonacci): "))

while(numero < 0):
    print("El numero debe ser positivo")
    numero = int(input("Ingrese un numero (Fibonacci)): "))

fibonacci = []
suma = 0
n_temp1 = 0
n_temp2 = 1

for i in range(1, numero):
    # print("i: ", i)
    suma = n_temp1 + n_temp2
    n_temp1 = n_temp2
    n_temp2 = suma
    if(suma > numero):
        break
    print(suma)





