name = '';
number = 0;
valientes = []
valiente = []

for i in range(0,3):
    valiente = []
    name = str(input("Ingrese su nombre valiente del reino: "))
    number = int(input("Ingrese un numero positivo caballero: "))
    while (number < 0):
        print("Alerta! solo los numeros positivos son bienvenidos")
        number = int(input("Ingrese un numero positivo caballero: "))
        if(number >= 0):
            break
    valiente.append(name)
    valiente.append(number)
    valientes.append(valiente)


for x in range(len(valientes)):
    for y in range(0, valientes[x][1]):
        print(f"{y+1}. {valientes[x][0]}")

    
print("Los valientes son: ", valientes)


# binario = 101011
binario = int(input("Ingrese el numero binario a descifrar: "))
binario_str = str(binario)[::-1]
binario_len = len(binario_str)
decimal = 0;

for r in range(0, binario_len):
    if(int(binario_str[r]) != 0):
        decimal += 2**r


print(f"El numero binario '{binario}' en decimal es: {decimal}")


# decimal = 450
decimal = int(input("Ingrese el numero decimal a descifrar: "))
binario = []
reduce_decimal = decimal

while(reduce_decimal >= 1):
    if(reduce_decimal % 2 == 0):
        binario.append('0')
    else:
        binario.append('1')

    # print(binario)
    reduce_decimal = int(reduce_decimal / 2);
    # print(reduce_decimal)
 
    
binario = "".join(binario)[::-1]

print(f"El numero decimal '{decimal}' en binario es: {binario}")
