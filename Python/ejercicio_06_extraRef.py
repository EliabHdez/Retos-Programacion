# FUNCIONES PASO DE VARIABLE POR REFERENCIA

motorcycles = ['CBR600RR', 'R6', 'H2R']
cars = ('Skyline', 'Lancer', 'Stratus')

# INTERCAMBIANDO LOS VALORES DE LAS VARIABLES ENTRE ELLAS

def change_values(list_1, tuple_1):
    change = list_1
    list_1 = tuple_1
    tuple_1 = change
    return list_1, tuple_1

vehicules = change_values(motorcycles, cars)
print(vehicules)

# ALMACENANDO RETORNO DE VALORES EN VARIABLES DIFERENTES A LAS ORIGINALES

print('----- Variables dif to or -----')

motos_to_cars = vehicules[0]
cars_to_motos = vehicules[1]

print(motos_to_cars)
print(cars_to_motos)

# IMPRESION VARIABLES ORIGINALES

print('----- Original variables -----')

print(f'* {motorcycles} *')
print(f'* {cars} *')

# MODIFICANDO LA LISTA Y LA TUPLA DENTRO DE LA FUNCION PARA GENERAR UN CAMBIO EN AMBAS AUN FUERA DE LA FUNCION

print('----- Modificacion -----')

def change_values(list_1, tuple_1):
    list_1.append('Pannigale')
    tuple_1 = list(tuple_1)
    tuple_1.append('Civic')
    tuple_1 = tuple(tuple_1)
    change = list_1
    list_1 = tuple_1
    tuple_1 = change
    global cars
    cars = list(cars)
    cars.append('Bora')
    cars = tuple(cars)
    return list_1, tuple_1

vehicules = change_values(motorcycles, cars)
print(vehicules)

# ALMACENANDO RETORNO DE VALORES EN VARIABLES DIFERENTES A LAS ORIGINALES

print('----- Variables dif to or -----')

motos_to_cars = vehicules[0]
cars_to_motos = vehicules[1]

print(motos_to_cars)
print(cars_to_motos)

# IMPRESION VARIABLES ORIGINALES

print('----- Original variables -----')

print(f'* {motorcycles} *')
print(f'* {cars} *')