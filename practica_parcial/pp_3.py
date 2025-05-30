# 3. Temperatura Descendente más Cercana

# arr_temperatures = [28, 35, 21, 18, 20, 32]
arr_temperatures = [28, 28, 35, 16, 40, 30]
new_temperatures = []

for i in range(len(arr_temperatures)):
    default = -1
    for t in range(i + 1, len(arr_temperatures)):
        if arr_temperatures[t] < arr_temperatures[i]:
            default = arr_temperatures[t]
            break
    new_temperatures.append(default)

print(new_temperatures)













