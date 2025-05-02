# Lab 3 - Segundo Corte

# Ticketera de cine

days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

total_ventas = 0

ninos = 12.000
adultos = 20.000
personas_mayores = 16.000

tickets_by_ninos = 0
tickets_by_adultos = 0
tickets_by_personas_mayores = 0

tickets_lunes = 0
tickets_martes = 0
tickets_miercoles = 0 
tickets_jueves = 0 
tickets_viernes = 0 
tickets_sabado = 0
tickets_domingo = 0

def cine_by_day(day):
    while True:
        print(f'''
        Precio de tickets - {day}
            
        1. Niños (12.000 $)
        2. Adultos (20.000 $)
        3. Personas Mayores (16.000 $) 
        ''')

        global tickets_by_ninos, tickets_by_adultos, tickets_by_personas_mayores
        categoria = int(input("Selecione el tipo de tikect que desea comprar: "))
        if(categoria == 1):
            ticket_price_selected = ninos
            tickets_by_ninos += 1
        elif(categoria == 2):
            ticket_price_selected = adultos
            tickets_by_adultos += 1
        elif(categoria == 3):
            ticket_price_selected = personas_mayores
            tickets_by_personas_mayores += 1
        else:
            print("Opción invalida")

        if(day.lower() == "martes" or day.lower() == "miercoles"):
            descuento = ticket_price_selected * 10 / 100
            ticket_price_selected = ticket_price_selected - descuento

        print("Compra exitosa ✅")
        global total_ventas
        total_ventas += ticket_price_selected
        
        global tickets_lunes, tickets_martes, tickets_miercoles, tickets_jueves, tickets_viernes, tickets_sabado, tickets_domingo

        if(day.lower() == "lunes"):
            tickets_lunes += 1
        elif(day.lower() == "martes"):
            tickets_martes += 1
        elif(day.lower() == "miercoles"):
            tickets_miercoles += 1
        elif(day.lower() == "jueves"):
            tickets_jueves += 1
        elif(day.lower() == "viernes"):
            tickets_viernes += 1
        elif(day.lower() == "sabado"):
            tickets_sabado += 1
        elif(day.lower() == "domingo"):
            tickets_domingo += 1
        else:
            print("Opción invalida")

        option = int(input("Selecione 1 para seguir vendiendo tickets o 0 para parar la venta: "))
        if(option != 1):
            print("loading next day...")
            break


for day in days: 
    cine_by_day(day)


print(f"El día Lunes se vendiero {tickets_lunes} tickets")
print(f"El día Martes se vendiero {tickets_martes} tickets")
print(f"El día Miercoles se vendiero {tickets_miercoles} tickets")
print(f"El día Jueves se vendiero {tickets_jueves} tickets")
print(f"El día Viernes se vendiero {tickets_viernes} tickets")
print(f"El día Sabado se vendiero {tickets_sabado} tickets")
print(f"El día Domingo se vendiero {tickets_domingo} tickets")

print(f"La cantidad de tickets se vendieron en la semana de Niños (12.000 $ c/u) es: {tickets_by_ninos}")
print(f"La cantidad de tickets se vendieron en la semana de Adultos (20.000 $ c/u) es: {tickets_by_adultos}")
print(f"La cantidad de tickets se vendieron en la semana de Personas Mayores (16.000 $ c/u) es: {tickets_by_personas_mayores}")

print(f"El total de ventas de la semana es: {total_ventas}$")

days_mas_vendidos = []
days_vendidos = [
    ["Lunes", tickets_lunes],
    ["Martes", tickets_martes],
    ["Miercoles", tickets_miercoles],
    ["Jueves", tickets_jueves],
    ["Viernes", tickets_viernes],
    ["Sabado", tickets_sabado],
    ["Domingo", tickets_domingo],

]

dia_mas_vendido = days_vendidos[0][1]
for i in range(len(days_vendidos)):
    if(dia_mas_vendido < days_vendidos[i][1]):
        dia_mas_vendido = days_vendidos[i][1]

for i in range(len(days_vendidos)):
    if(dia_mas_vendido == days_vendidos[i][1]):
        print(f"El día más vendido fue el  {days_vendidos[i][0]} con un total de {days_vendidos[i][1]} tickets vendidos")


# Lista de numeros

lista_numeros = [3,4,5,6,7,10,12,4,7,12,121,98,661,2,99]
total_suma_lista_numeros = 0
numnero_min = lista_numeros[0]
numnero_max = lista_numeros[0]

for numero in lista_numeros:
    if(numero < numnero_min):
        numnero_min = numero
    if(numero > numnero_max):
        numnero_max = numero
    total_suma_lista_numeros += numero



print(f"El numero menor de la lista de numeros es {numnero_min}")
print(f"El numero mayor de la lista de numeros es {numnero_max}")
print(f"El total de la suma de la lista de numeros es {total_suma_lista_numeros}")
print(f"La cantidad de numeros de la lista es: {len(lista_numeros)}")
lista_numeros.sort()
print(f"Lista de numeros ordenada ascendente es: {lista_numeros}")


# ASC menor a mayor
# DESC mayor a menor