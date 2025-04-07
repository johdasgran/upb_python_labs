# Laboratorio 2 - Segundo Corte

# Calcular el factorial de un numero entero positivo 

# numero = int(input("Ingrese un numero: "))
# factorial = 0

# while(numero < 0):
#     print("El numero debe ser positivo")
#     numero = int(input("Ingrese un numero: "))

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

# for i in range(numero, 0, -1):
#     i_temp = i-1
#     if(i == numero):
#         factorial = i*i_temp
#     if(i != numero and i_temp != 0):
#         factorial = factorial*i_temp

# print(f"El factorial es: {factorial}")

# Imprimir los primeros n numeros de la serie Fibonacci

numero = int(input("Ingrese un numero: "))
fibonacci = []
suma = 0
n_temp1 = 0
n_temp2 = 1

for i in range(1, numero+1):
    # print("i: ", i)
    n_temp1 = n_temp1 + n_temp2
    n_temp2 = n_temp1
    # suma = n_temp1 + n_temp2
    # print(suma)
    if(n_temp1 > numero):
        break
    # print("t1", n_temp1)
    print("t2", n_temp2)