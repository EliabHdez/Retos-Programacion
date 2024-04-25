# --- Excepciones ---

try:
    div = 10 / 0
    print(div)
except ZeroDivisionError:
    print('Error: No se puede dividir entre 0')
finally:
    print('Este es el finally')

print('*** Continua la ejecución del programa ***')

cars = ['Stratus', 'Neon']

# print(cars[2])

try:
    print(cars[0])
    print(cars[1])
    print(cars[2])
except IndexError as error:
    print(error)
    print('No hay ningun elemento en la posicion 2 de la lista')
finally:
    print('*** Fin del programa ***')
    
num_1 = 5
num_2 = '9'

num_2 = int(num_2)

try:
    suma = num_1 + num_2
except:
    print('Datos erroneos')
else:
    print('Los datos son correctos')
    print('Generando el resultado...')
    print(suma)
finally:
    print('Final del intento de suma')
    
num_1 = 5
num_2 = '9'

try:
    suma = num_1 + num_2
except TypeError as error:
    print('Datos erroneos')
    print(f'Error detectado: {error}')
else:
    print('Los datos son correctos')
    print('Generando el resultado...')
    print(suma)
finally:
    print('Final del intento de suma')
    
# --- EJERCICIO EXTRA ---

""" 
    Crea una función que sea capaz de procesar parámetros, pero que también pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que corresponderse con un tipo de excepción creada por nosotros de manera personalizada, y debe ser lanzada de manera manual) en caso de error.
        - Captura todas las excepciones desde el lugar donde llamas a la función.
        - Imprime el tipo de error.
        - Imprime si no se ha producido ningún error.
        - Imprime que la ejecución ha finalizado.
"""

print('')
print('--- EXTRA ---')
print('')

# def procesar_parametros(name, lastname, age, job):
    
#     def errores():
        
        
#     try:
#         name + age
#     except:
#         print('No es posible sumar un nombre con una edad')
#     else:
#         print('No se ha encontrado ningún error')
#         print('Suma realizada con éxito')
#     finally:
#         print('Fin intento concatenar nombre + edad')
        
#     try:
#         name = str()
#     except:
#         print('El nombre tiene que ser una cadena de texto')
#     else:
#         print('No se ha encontrado ningún error')
#         print('Nombre registrado correctamente')
#     finally:
#         print('Comprobación de nombre ejecutada con éxito')
        
#     try:
#         job != lastname
#     except:
#         print('El apellido tiene que ser diferente a la profesion')
#     else:
#         print('No se ha encontrado ningún error')
#         print('Apellido registrado correctamente')
#     finally:
#         print('Comprobación de apellido finalizada')
        
# par_errors('Moises', 'Programador', 33, 'Programador')

class StrTypeError(Exception):
    pass

def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto.")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)


try:
    process_params([1, 2, 3, 4])
except IndexError as e:
    print("El número de elementos de la lista debe ser mayor que dos.")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido ningún error.")
finally:
    print("El programa finaliza sin detenerse.")