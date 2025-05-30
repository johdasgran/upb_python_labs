# 1. Suma Objetivo en una Pasada - con lista (lento, compara 1 a 1) "if in"

arr = [5, 8, 12, 2, 7, 100, 32, 3]
n_objetvo = 8

suma_arr = []

for value in arr:
    left = n_objetvo - value
    if left in arr:
        suma_arr = [value, left]
        break
        
print(suma_arr)


# 1. Suma Objetivo en una Pasada - con set (rapido, busca directo por hash) "if in"

arr = [5, 8, 12, 2, 7, 100, 32, 3]
n_objetvo = 8

vistos = set()
suma_arr = []

for value in arr:
    left = n_objetvo - value
    if left in vistos:
        suma_arr = [left, value]
        break
    vistos.add(value)

print(suma_arr)











