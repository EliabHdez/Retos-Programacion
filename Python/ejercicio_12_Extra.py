""" 
    Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt
        - Cada producto se guarda en una línea del archivo de la siguiente manera:              
            [nombre_producto], [cantidad_vendida], [precio].
        - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,actualizar, eliminar productos y salir.
        - También debe poseer opciones para calcular la venta total y por producto.
        - La opción salir borra el .txt.
"""

import os

def sales_manager():
    print('What do you want?\n 1.- Create a new sales file\n 2.- Add sale\n 3.- Consult sales manager\n 4.- Exit')
    choice = input('Enter the number your choice: ')
    
    try:
        choice = int(choice)
    except Exception as error:
        print('You must enter the number corresponding to the desired option as a response')
    else:
        print('Processing your request...')
        
    if choice == 1:
        sales_file = open('Files/sales_file.txt', 'w+')
        print(sales_file)
        
    if choice == 2:
        add_sale()
        
    if choice == 3:
        consult()
        
    if choice == 4:
        print('Leaving the program...')
        
def add_sale():
    product = input('Enter the product sold: ')
    quantity = int(input('Enter the quantity sold: '))
    price = float(input('Enter the price of product: $'))
    choice = input('If the sales file does not exist, it will be created.\nDo you wish to continue? [y/n]: ').lower()
    print('Executing...')
    if choice == 'yes' or choice == 'y':
        sales_file = open('Files/sales_file.txt', 'a')
        sales_file.write(f'[Product: {product}] -> [Amount: {quantity}] -> [Price: {price}]\n')
        sales_file.close()
    elif choice == 'no' or choice == 'n':
        print('Choice the option "1" to create a sales file. This option (2) is to add a new sale to the existing file')
        
def consult():
    try:
        sales_file = open('Files/sales_file.txt', 'r+')
        print(sales_file.read())
        sales_file.close()
    except:
        print('The file "sales_file" does not exist')
        
sales_manager()