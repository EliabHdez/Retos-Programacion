""" 
    EJERCICIO:
    
    - Desarrolla un programa capaz de crear un archivo que se llame como tu usuario de GitHub y tenga la extensión .txt.
    - Añade varias líneas en ese fichero:
        - Tu nombre.
        - Edad.
        - Lenguaje de programación favorito.
    - Imprime el contenido.
    - Borra el fichero.
    
    DIFICULTAD EXTRA (opcional):
    
    - Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
    - Cada producto se guarda en una línea del archivo de la siguiente manera: [nombre_producto], [cantidad_vendida], [precio].
    - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
    - También debe poseer opciones para calcular la venta total y por producto.
    - La opción salir borra el .txt.
"""

import os
# import re

print('What do you want?\n1.- Create new file\n2.- View file content\n3.- Remove file')

try:
    file_option = int(input('Enter the desired option: '))
    if file_option == 1:
        file_name = input('Write the name to the new file: ')
        print(f'Will be create the file with the name: "{file_name}"')
        file_name = str(file_name)
        file_created = open(f'Python/{file_name}.txt', 'w+')
        print('The file must contain the following data:\n - Name\n - Age\n - Sex\n - Git Username')
        name = input('Enter your name: ').capitalize()
        age = input('Enter your age: ')
        sex = input('Enter your sex: ').capitalize()
        git_user = input('Enter your git username: ').lower()
        print('"Entering data into the file..."')
        file_created.write(f'Name: {name}\n')
        file_created.write(f'Age: {age}\n')
        file_created.write(f'Sex: {sex}\n')
        file_created.write(f'Git Username: {git_user}')
        print('"Data entered"')
        print('What do you want?\n1.- View file content\n2.- Exit')
        choice = input('Enter your choice: ')
        # choice = re.findall('\d+', option_1)
        # choice = choice[0]
        choice = int(choice)
        if choice == 1:
            file_created = open(f'Python/{file_name}.txt', 'r+')
            print(file_created.read())
            file_created.close()
        elif choice == 2:
            file_created.close()
            print('Exiting...')
            print('Nice day!')
    elif file_option == 2:
        file_name = input('Enter the file name what do you want to see: ')
        try:
            file_view = open(f'Python/{file_name}.txt', 'r+')
            print(file_view.read())
            file_view.close()
        except Exception as error:
            print(f'The file "{file_name}" does not exist. ("{error}")')
            print('Exiting the program...')
    elif file_option == 3:
        file_name = input('Write the name file to want remove it: ')
        try:
            os.remove(f'Python/{file_name}.txt')
        except Exception as error:
            print(f'The file "{file_name}" does not exist. ("{error}")')
        else:
            print(f'The file "{file_name.upper()}" will be deleted')
            print('Deleting...')
            print('File successfully deleted')
        finally:
            print('Exiting the program...')
            print('Have a nice day!!!')
    else:
            print('Options to answers: "1" or "2".')
except:
        print("Answers that are not numerical are not allowed")
    
""" # file_modification = input('Que desea hacer con el archivo creado?\n 1.- Agregar contenido\n 2.- Leer el contenido\n 3.- Agregar contenido y depues leer archivo')

user_git = open('Python/eliab_hdez.txt', 'w')

user_git.write('Name: Moisés Hernandez\n')
user_git.write('Edad: 33 años\n')
user_git.write('Lenguajes de programación favoritos: Python y C++')

user_git = open('Python/eliab_hdez.txt', 'r+')

print(user_git.read())

user_git = open('Python/eliab_hdez.txt', 'w')
user_git.write('\nProyectos actuales en mente')

user_git = open('Python/eliab_hdez.txt', 'r')
print(user_git.read())

user_git.close()
    
user_git = open('Python/eliab_hdez.txt', 'w')
user_git.write('\n- Aplicacion movil para personas con problemas auditivos')
user_git = open('Python/eliab_hdez.txt', 'r')
print(user_git.read())

user_git.close()

# os.remove('Python/eliab_hdez.txt') """