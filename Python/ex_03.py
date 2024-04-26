# Funciones y alcance

def language():
    print('Python')

def get_name(name):
    print(name)
    
language()    
get_name('Moises')

def suma(num_one, num_two):
    num_one + num_two
    
suma(5, 9)

def resta(num_one, num_two):
    return num_one - num_two

print(resta(5, 9))

def person_data(age, alias, name):
    print(name, age, alias)
    
person_data('Predator', 'Moises', 33)
person_data(name='Moises', alias='Predator', age=33)

def video_games(juego, consola_compatible, genero = 'No definido'):
    games = (juego, consola_compatible, genero)
    for element in games:
        print(element)
        
video_games('God of War', 'PS4 y PS5')
print('------------------')

video_games('Halo 4', 'Xbox360, XboxOne y Xbox Series X')
print('------------------')

video_games('The Last of Us', 'PS4 y PS5', 'Terror, Suspenso')
print('------------------')

video_games('Titanfall 2', 'PS4, PS5, XboxOne, Xbox Series X', 'Acción')
print('------------------')

def get_full_name(full_name):
    def comp_name():
        print(f'Nombre ingresado: {full_name}')
        print('--- Iniciando comprobación... ---')
        if type(full_name) != str:
            print('Nombre ingresado NO válido')
            print('--- Comprobación de nombre finalizada ---')
        if type(full_name) == str:
            try:
                int(full_name)
            except:
                print('Nombre válido e ingresado con éxito')
            else:
                print(f'Nombre ingresado NO válido. ({full_name})')
            finally:
                print('--- Comprobación de nombre finalizada ---')
    comp_name()
                
get_full_name('Moisés Hernández')
get_full_name('33')
get_full_name(33)
get_full_name(True)

my_name = 'Moises' # Variable global -> Declara fuera de una función. Accesible desde cualquier lugar en el código

def name_one(apellido):
    name_funcion = 'Eliab' # Variable local -> Definida dentro de la función. Solo es accesible dentro de la misma
    print(name_funcion, apellido) # La varible "apellido" tambien es una variable local
    print(my_name) # Variable global referenciada en la función
    
print(my_name)
name_one('Hernandez')

print('*********************** EJERCICIO EXTRA *****************************')

# No fui capaz de resolverlo por mi cuenta, estuve cerca, tenia mal la sintaxis...

""" 
    def imp_numbers(multiplo_tres, multiplo_cinco):
        contador = 0
        for e in range(1, 10):
            e += 1
            print(e)
            if e % 3 == 0:
                print(multiplo_tres)
            if e % 5 == 0:
                print(multiplo_cinco)
            if e % 3 == 0 and e % 5 == 0:
                print(f'{multiplo_tres} - {multiplo_cinco}')
            contador += 1        
    return print(contador)
"""

def imp_numbers(multiplo_tres, multiplo_cinco):
    contador = 0     
    for e in range(1, 10):
        if e % 3 == 0:
            print(multiplo_tres)
        elif e % 5 == 0:
            print(multiplo_cinco)
        elif e % 3 == 0 and e % 5 == 0:
            print(f'{multiplo_tres} - {multiplo_cinco}')
        else:
            print(e)
            contador += 1        
    return print(contador)
            
imp_numbers('M3', 'M5')

print('---------------- Solución Brais ---------------------')

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 10):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return print(count)

print_numbers('M3 ', 'M5')

print('---------------- Ejercicio completo ---------------------')

# Este es el ejercicio como tal, hasta el numero 100

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return print(count)

print_numbers('M3 ', 'M5')