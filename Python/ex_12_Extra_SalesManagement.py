""" 
    EJERCICIO: 
    - Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
    - Cada producto se guarda en una línea del archivo de la siguiente manera: [nombre_producto], [cantidad_vendida], [precio].
    - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
    - También debe poseer opciones para calcular la venta total y por producto.
    - La opción salir borra el .txt.
"""

# Importing the os module to work with files
import os

# Main function
# Function responsible for controlling the program
def sales_Manager():
    print('')
    print('What do you want?\n 1.- Create a new file\n 2.- Add sale\n 3.- Add product\n 4.- Consult sales manager or inventories\n 5.- Check existing files\n 6.- Exit')
    choice = input('Enter the number your choice: ')
    
    try:
        choice = int(choice)
    except:
        print('"You must enter the number corresponding to the desired option as a response"')
        sales_Manager()
    else:
        print('Processing your request...\n')
        
        if choice <= 0 or choice >= 7:
            print('"Error answer. Try again"')
            sales_Manager()
            
        if choice == 1:
            create_File()
            
        if choice == 2:
            add_Sale()
            
        if choice == 3:
            add_Inventory()
            
        if choice == 4:
            consult()
            
        if choice == 5:
            available_Files()
            
        if choice == 6:
            print('Leaving the program...')
        
        
# Function to create new file
def create_File():
    print('What type file do you want to create?\n 1.- Sales\n 2.- Inventory')
    create_file = input('Enter your number choice: ')
    try:
        create_file = int(create_file)
        if create_file <= 0 or create_file >= 3:
            print('Error answer: "Please enter 1 or 2"\n')
            create_File()
        else:
            print('Initializing...')
    except:
        print('Answer error: Please enter 1 or 2\n')
        create_File()
        
    if create_file == 1:
        print('"New sales file"')
        name_file = input('Name file: ')
        if name_file == 'exit' or name_file == 'Exit':
            create_File()
        else:
            sales_file = open(f"C:/Python/Files/Sales/{name_file}.txt", 'w+')
            print(f'"{name_file}" was created succesfully')
    elif create_file == 2:
        print('"New inventory"')
        name_file = input('Name file: ')
        if name_file == 'exit' or name_file == 'Exit':
            create_File()
        else:
            inv_file = open(f'C:/Python/Files/Inventories/{name_file}.txt', 'w+')
            print(f'"{name_file}" was created succesfully')
        
    sales_Manager()
        
# Function to add sales
def add_Sale():
    product = input('Enter the product sold: ')
    quantity = int(input('Enter the quantity sold: '))
    price = float(input('Enter the unit price: $'))
    total_price = quantity * price
    print('"Available files"')
    available_files = os.listdir('C:/Python/Files/Sales')
    if len(available_files) == 0:
        print('No sales files available')
    else:
        for element in available_files:
            print(f' - {element}')
    choice = input('If the sales file does not exist, it will be created.\nDo you wish to continue? [y/n]: ').lower()
    print('Executing...')
    if choice == 'yes' or choice == 'y':
        name_file = input('Enter the name file (without extension) where the sale will be saved: ').lower()
        sales_file = open(f'C:/Python/Files/Sales/{name_file}.txt', 'a')
        sales_file.write(f'[Product: {product.capitalize()}] -> [Amount: {quantity}] -> [Unit Price: ${price}] -> [Total: ${total_price}]\n')
        sales_file.close()
        print('Successfully added sale')
    elif choice == 'no' or choice == 'n':
        print('To create a new file, choice the 1 option.')
        
    sales_Manager()
    
# Function to add to the inventory
def add_Inventory():
    product = input('Enter the product to add: ')
    price = float(input('Enter the unit price: $'))
    print('"Available files"')
    available_files = os.listdir('C:/Python/Files/Inventories')
    if len(available_files) == 0:
        print('No inventories files available')
    else:
        for element in available_files:
            print(f' - {element}')
    choice = input('If the inventory file does not exist, it will be created.\nDo you wish to continue? [y/n]: ').lower()
    print('Executing...')
    if choice == 'yes' or choice == 'y':
        name_file = input('Enter the name file (without extension) where the sale will be saved: ').lower()
        sales_file = open(f'C:/Python/Files/Inventories/{name_file}.txt', 'a')
        sales_file.write(f'{product.capitalize()} -> ${price}\n')
        sales_file.close()
        print('Product added to inventory successfully')
    elif choice == 'no' or choice == 'n':
        print('To create a new file, choice the 1 option.')
        
    sales_Manager()
        
# Function to review sales 
def consult():
    print('What do you want review?\n 1.- Sales management\n 2.- Inventories\n 3.- Exit')
    review_file = input('Please enter your answer: ')
    
    if review_file == '3' or review_file == 'exit' or review_file == 'Exit':
        print('Leaving...')
        sales_Manager()
    else:
        try:
            review_file = int(review_file)
            if review_file <= 0 or review_file >= 4:
                print('"Error answer"\n')
                consult()
            if review_file == 1:
                availables_sales_files = os.listdir('C:/Python/Files/Sales')
                for element in availables_sales_files:
                    print('\n"Sales"')
                    print(f'  - {element}')
                name_file = input('Enter the name file what you want to review (without extension): ')
                if name_file == 'exit' or name_file == 'Exit':
                    sales_Manager()
                else:
                    try:
                        sales_file = open(f'C:/Python/Files/Sales/{name_file}.txt', 'r+')
                        print(sales_file.read())
                        sales_file.close()
                        consult()
                    except:
                        print(f'The file "{name_file}" does not exist')
                
            if review_file == 2:
                availables_inventories_files = os.listdir('C:/Python/Files/Inventories')
                for element in availables_inventories_files:
                    print('"Inventories"')
                    print(f'  - {element}')
                name_file = input('Enter the name file what you want to review (without extension): ')
                if name_file == 'exit' or name_file == 'Exit':
                    sales_Manager()
                else:
                    try:
                        sales_file = open(f'C:/Python/Files/Inventories/{name_file}.txt', 'r+')
                        print(sales_file.read())
                        sales_file.close()
                        consult()
                    except:
                        print(f'The file "{name_file}" does not exist')
        except:
            print('"Error answer": Please select any to options availables')
            consult()
        
def available_Files():
    available_sales_files = os.listdir('C:/Python/Files/Sales')
    available_inventory_files = os.listdir('C:/Python/Files/Inventories')
    if len(available_sales_files) == 0 and len(available_inventory_files) == 0:
        print('"There are not any files in existence"')
    else:
        sales_inventories = available_sales_files + available_inventory_files
        for element in sales_inventories:
            print(f'- {element}')
            
    sales_Manager()

# Main function call
sales_Manager()
