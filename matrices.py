# Python Matrices

# SIN USAR FUNCIONES PREDETERMINADAS DE NINGÚN 
# LENGUAJE DESARROLLE LOS SIGUIENTES EJERCICIOS:

# Para ejecutar cada ejericio solo tiene que 
# descomentar los comentarios de la función 
# para la prueba :)


# 1. Crea una matriz de tamaño 3x3 y muestra todos 
# sus elementos.

def create_array():
    array3x3 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    for i in range(len(array3x3)):
        print(f"Elementos fila {i}: ")
        for j in range(len(array3x3[i])):
            print(f"Elemento en posición array3x3[{i}][{j}] {array3x3[i][j]}")


# create_array()

# 2. Resta dos matrices de tamaño 2x2 y muestra el resultado.

def resta_matrices():
    matriz1 = [
        [1, 2],
        [8, 9]
    ]
    matriz2 = [
        [3, 4],
        [6, 7]
    ]
    nueva_matriz = []

    if(len(matriz1) == len(matriz2)):
        for i in range(len(matriz1)):
            fila = []
            for j in range(len(matriz2)):
                value = matriz1[i][j] - matriz2[i][j]
                fila.append(value)
            nueva_matriz.append(fila)
        print(f"La resta de las dos matrices es: {nueva_matriz}")


# resta_matrices()

# 3. Encuentra el número más grande en un array y muestra su valor.

def find_max_array():
    array = [1,4,5,8,12,3,99,23,111,66,1,42]
    n_max = array[0]
    for i in range(len(array)):
        if(array[i] > n_max):
            n_max = array[i];
    print(f"El numero mayor es: {n_max}")


# find_max_array()

# 4. Calcule el cuadrado de todos los elementos de una 
# lista de n elementos, agregue el resultado a una 
# nueva lista y ordene el resultado de menor a mayor


def cuadrado_lista():
    lista = [1,9,5,4,3,7,6,8,2]
    lista_sorted = []
    lista_cuadrado = []

    temp_lista = lista;
    for x in range(len(lista)):
        n_min = find_min_array(temp_lista)
        temp_lista.remove(n_min)
        lista_sorted.append(n_min)

    for i in range(len(lista_sorted)):
        value = lista_sorted[i]*lista_sorted[i]
        lista_cuadrado.append(value)

    print(f"Cuadrados de lista ordenada menor a mayor {lista_cuadrado}")


def find_min_array(lista):
    n_min = lista[0]
    for x in range(len(lista)):
        if(lista[x] < n_min):
            n_min = lista[x]
    return n_min

# cuadrado_lista()

# 5. Cuenta cuántas veces aparece un número específico 
# en un array y muestra el resultado.

def count_repeat_element(lista, number_to_find):
    count = 0;
    for i in range(len(lista)):
        if(lista[i] == number_to_find):
            count += 1

    print(f"El numero {number_to_find} se repite {count} veces")


# list = [88,88,12,2,3,4,5,7,9,3,2,2,2,1,1,6]
# list_number_to_find = 2
# count_repeat_element(list, list_number_to_find)

# 6. Verifica si dos vectores son iguales y muestra el resultado.

def equals_array(arr1, arr2):
    message = ''
    if(len(arr1) == len(arr2)):
        for i in range(len(arr1)):
            if(arr1[i] != arr2[i]):
                return print(f"Los arrays {arr1} y {arr2} no son iguales")
        return print(f"Los arrays {arr1} y {arr2} son iguales")
    return print(f"Los arrays {arr1} y {arr2} no son iguales")                        


# arr1 = [1,2,3,4,5]
# arr2 = [1,2,4,4,5]
# equals_array(arr1, arr2)