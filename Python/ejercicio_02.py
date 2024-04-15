# Operadores

print('-------- Operadores aritméticos ---------')

# Operadores aritméticos

suma = 2 + 2
resta = 5 - 1
multiplicacion = 9 * 6
division = 7 / 3
exponente = 8 ** 4
modulo = 10 % 3
division_entera = 10 // 3


print(resta)
print(multiplicacion)
print(division)
print(exponente)
print(modulo)
print(division_entera)

print('-------- Operadores de comparación ---------')

# Operadores de comparación

igual = True == False
mayor_que = 10 > 5
menor_que = 10 < 5
mayor_igual = 3 >= 4
menor_igual = 3 <= 4
diferente = True != False

print(suma)
print(igual)
print(mayor_que)
print(menor_que)
print(mayor_igual)
print(menor_igual)
print(diferente)

print('-------- Operadores lógicos ---------')

# Operadores lógicos

operador_and_one = 'Hola' == 'Hola' and 'hola' != 'ola'
operador_and_two = 'Hola' == 'Hola' and 'hola' == 'ola'
operador_and_three = 'Hola' == 'hola' and 'hola' == 'ola'

operador_or_one = 'Hola' == 'Hola' and 'hola' != 'ola'
operador_or_two = 'Hola' == 'Hola' and 'hola' == 'ola'
operador_or_three = 'Hola' == 'hola' and 'hola' == 'ola'

operador_not_one = not False
operador_not_two = not True
operador_not_three = not True == False

print(operador_and_one)
print(operador_and_two)
print(operador_and_three)
print(operador_or_one)
print(operador_or_two)
print(operador_or_three)
print(operador_not_one)
print(operador_not_two)
print(operador_not_three)

print('-------- Operadores de asignación ---------')

my_number = 11  # asignación
print(my_number)

my_number += 1  # suma y asignación
print(my_number)

my_number -= 1  # resta y asignación
print(my_number)

my_number *= 2  # multiplicación y asignación
print(my_number)

my_number /= 2  # división y asignación
print(my_number)

my_number %= 2  # módulo y asignación
print(my_number)

my_number = 2
my_number **= 3  # exponente y asignación
print(my_number)

my_number //= 3  # división entera y asignación
print(my_number)

print('-------- Operadores de pertenencia ---------')

# Los operadores de pertenencia son "in" y "not in"

print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")

name = 'Moises'
letra_one = 's' in name
letra_two = 'c' in name

print(f'La letra "s" esta en el nombre {name}: {letra_one}')
print(f'La letra "c" esta en el nombre {name}: {letra_two}')

print('**************************************************')

print('-------- Condicionales ---------')

number_one = 5
number_two = 9

if number_one < number_two:
    print(f'El numero {number_one} es menor que {number_two}')
elif number_one == number_two:
    print(f'El numero {number_one} es igual a {number_two}')
elif number_one > number_two:
    print(f'El numero {number_one} es mayor que {number_two}')
else:
    print('Los datos ingresados no son numericos')
    
number_one = 6
number_two = 6
    
if number_one < number_two:
    print(f'El numero {number_one} es menor que {number_two}')
elif number_one == number_two:
    print(f'El numero {number_one} es igual a {number_two}')
elif number_one > number_two:
    print(f'El numero {number_one} es mayor que {number_two}')
else:
    print('Los datos ingresados no son numericos')
    
number_one = 9
number_two = 5
    
if number_one < number_two:
    print(f'El numero {number_one} es menor que {number_two}')
elif number_one == number_two:
    print(f'El numero {number_one} es igual a {number_two}')
elif number_one > number_two:
    print(f'El numero {number_one} es mayor que {number_two}')
else:
    print('Los datos ingresados no son numericos')
    
number_one = 5
number_two = 'Python'
    
if type(number_one) == int and type(number_two) != int:
    print(f'Segundo dato ingresado no es de tipo numerico. Tipo de dato: {type(number_two)}')
elif type(number_one) != int and type(number_two) == int:
    print(f'Primer dato ingresado no es de tipo numerico. Tipo de dato: {type(number_one)}')
elif type(number_one) == type(number_two):
    print(f'Los datos ingresados no son numericos. Tipo de datos ingresados: {type(number_one)} ')
elif type(number_one) != type(number_two):
    print(f'Los datos ingresados no son numericos. Tipo de datos ingresados: 1.- {type(number_two)}, 2.- {type(number_two)}')
    
number_one = 'Hola'
number_two = 6
    
if type(number_one) == int and type(number_two) != int:
    print(f'Segundo dato ingresado no es de tipo numerico. Tipo de dato: {type(number_two)}')
elif type(number_one) != int and type(number_two) == int:
    print(f'Primer dato ingresado no es de tipo numerico. Tipo de dato: {type(number_one)}')
elif type(number_one) == type(number_two):
    print(f'Los datos ingresados no son numericos. Tipo de datos ingresados: {type(number_one)} ')
elif type(number_one) != type(number_two):
    print(f'Los datos ingresados no son numericos. Tipo de datos ingresados: 1.- {type(number_two)}, 2.- {type(number_two)}')
    
number_one = True
number_two = 'Python'
    
if type(number_one) == int and type(number_two) != int:
    print(f'Segundo dato ingresado no es de tipo numerico. Tipo de dato: {type(number_two)}')
elif type(number_one) != int and type(number_two) == int:
    print(f'Primer dato ingresado no es de tipo numerico. Tipo de dato: {type(number_one)}')
elif type(number_one) == type(number_two):
    print(f'Los datos ingresados no son numericos. Tipo de datos ingresados: {type(number_one)} ')
elif type(number_one) != type(number_two):
    print(f'Los datos ingresados no son numericos. Tipo de datos ingresados: 1.- {type(number_one)}, 2.- {type(number_two)}')
    
print('**************************************************')

print('-------- Iterativas ---------')
    
# interes_persona = input('Escriba el tipo de vehiculo que esta buscando. Carro o Moto: ')

carro = ['Stratus', 2005, 'R/T', '2.4 lts Turbo']
moto = ['Honda', 2005, 'CBR600RR', '600cc']

interes_persona = 'CARRO'
interes_persona = interes_persona.lower()

while interes_persona == 'carro':
    print(f'Tenemos el siguiente carro disponible: {carro}')
    break

interes_persona_dos = 'MOTO'
interes_persona_dos = interes_persona_dos.lower()
    
while interes_persona_dos == 'moto':
    print(f'Tenemos la siguiente moto disponible: {moto}')
    break

i = 0

while i <= 10:
    print(i)
    i += 1

print('**************************************************')

print('Datos del carro:')
for element in carro:
    print(element)
    
print('**************************************************')
    
print('Datos de la motocicleta:')
for element in moto:
    print(element)
    
print('**************************************************')
    
for element in moto:
    print('El modelo la motocicleta es el siguiente:') # Esta línea la imprimio todas las veces que fueron necesarias dentro de la tupla hasta que llego al elemento 'CBR600RR'
    if element == 'CBR600RR':
        print(element)
        break
else:
    print('Esperemos le haya sido útil la información')
    
print('**************************************************')
    
for element in moto:
    print(element)
    if element == 'CBR600RR':
        print('Es el modelo de la motocicleta disponible actualmente')
else:
    print('Esperemos le haya sido útil la información')
    
print('-------- Manejo de excepciones ---------')

name = 'Moises'
lastname = 'Hernandez'
age = 33

try:
    name + age
except:
    print('No se pueden concatenar strings con int')
else:
    try:
        name + lastname
    except:
        print('Nombre y apellido no validos')
finally:
    print(f'Datos ingresados: Nombre: {name}, Apellido: {lastname}, Edad: {age}')
    
print('-------------------------------------------')
    
name = 'Moises'
lastname = 'Hernandez'
age = 33

try:
    print(f'{name} {lastname}')
except:
    print('No se pueden concatenar strings con int')
else:
    print('Los datos ingresados son validos')
finally:
    print(f'Datos ingresados: Nombre: {name}, Apellido: {lastname}, Edad: {age} años')
    
print('*********************** EJERCICIO EXTRA *****************************')

# Ejercicio extra

# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

num = 10

while num < 55:
    if num == 10:
        print(num)
    num += 2
    if num % 3 != 0 and num != 16:
        print(num)
    if num == 52:
        num += 3
        print(num)
        break
        
print('**************************************************')
        
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)