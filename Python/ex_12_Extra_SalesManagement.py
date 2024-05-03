""" 
    Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt
        - Cada producto se guarda en una línea del archivo de la siguiente manera:              
            [nombre_producto], [cantidad_vendida], [precio].
        - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
        - También debe poseer opciones para calcular la venta total y por producto.
        - La opción salir borra el .txt.
"""

# Agregar exit a la funcion add_sale (opcional)
# Agregar exit a la funcion add_product (opcional)
# Programar que cuando se agreguen productos a los inventarios por primera vez, estos se acomoden por orden alfabetico (como cuando actualizan los inventarios) por si ingresan los productos como vayan cayendo

# Importing the os module to work with files
import os

# Main function
# Function responsible for controlling the program
def sales_Manager():
    print('')
    print('What do you want?\n 1.- Create a new file\n 2.- Add sale\n 3.- Add product\n 4.- Consult sales manager or inventories\n 5.- Review existing files\n 6.- Update stock\n 7.- Delete product\n 8.- Exit')
    choice = input('Enter the number of your choice: ')
    
    if choice == 'Exit' or choice == 'exit' or choice == '8':
        print('Leaving the program...')
        print('Nice day!')
    else:
        try:
            choice = int(choice)
            if choice <= 0 or choice >= 9:
                print('"Error answer. Try again"')
                sales_Manager()
            if choice >= 1 and choice <= 7:
                print('Processing your request...\n')
        except:
            print('"You must enter as answer the number corresponding to the desired option"')
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
            update_data()

        if choice == 7:
            remove_data()
        
# Function to create new file
def create_File():
    print('What type file you want to create?\n 1.- Sales\n 2.- Inventory')
    create_file = input('Enter your number choice: ')
    try:
        create_file = int(create_file)
        if create_file <= 0 or create_file >= 3:
            print('Answer error: "Please enter 1 or 2"\n')
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
            sales_file = open(f'Python/Files/Sales/{name_file}.txt', 'w+')
            print(f'"{name_file}" was succesfully created')
    elif create_file == 2:
        print('"New inventory"')
        name_file = input('Name file: ')
        if name_file == 'exit' or name_file == 'Exit':
            create_File()
        else:
            inv_file = open(f'Python/Files/Inventories/{name_file}.txt', 'w+')
            inv_file.write('"Products --- No. de piezas"')
            print(f'"{name_file}" was succesfully created')
        
    sales_Manager()
        
# Function to add sales
def add_Sale():
    product = input('Enter the sold product: ')
    quantity = int(input('Enter the quantity sold: '))
    price = float(input('Enter the unit price: $'))
    total_price = quantity * price
    print('"Available files"')
    available_files = os.listdir('Python/Files/Sales')
    if len(available_files) == 0:
        print('No sales files available')
    else:
        for element in available_files:
            print(f' - {element}')
    choice = input('If the sales file does not exist, it will be created.\nDo you wish to continue? [y/n]: ').lower()
    print('Executing...')
    if choice == 'yes' or choice == 'y':
        name_file = input('Enter the name file (without .txt) where the sale will be uploaded: ').lower()
        sales_file = open(f'Python/Files/Sales/{name_file}.txt', 'a')
        sales_file.write(f'[Product: {product.capitalize()}] -> [Amount: {quantity}] -> [Unit Price: ${price}] -> [Total: ${total_price}]\n')
        sales_file.close()
        print('Successfully added sale')
    elif choice == 'no' or choice == 'n':
        print('To create a new file, select option 1.')
        
    sales_Manager()
    
# Function to add to the inventory
def add_Inventory():
    product = input('Enter the product to add: ')
    pieces = int(input('Enter the number of pieces: '))
    print('"Available files"')
    available_files = os.listdir('Python/Files/Inventories')
    if len(available_files) == 0:
        print('No inventories files available')
    else:
        for element in available_files:
            print(f' - {element}')
    choice = input('If the inventory file does not exist, it will be created.\nDo you wish to continue? [y/n]: ').lower()
    print('Executing...')
    if choice == 'yes' or choice == 'y':
        name_file = input('Enter the name file (without .txt) where the sale will be uploaded: ').lower()
        sales_file = open(f'Python/Files/Inventories/{name_file}.txt', 'a')
        sales_file.write(f'{product.capitalize()} - {pieces} pzas\n')
        sales_file.close()
        print('Product successfully added to inventory')
    elif choice == 'no' or choice == 'n':
        print('To create a new file, choice the 1 option.')
        
    sales_Manager()
        
# Function to review sales
def consult():
    print('What do you want review?\n 1.- Sales Manager\n 2.- Inventories\n 3.- Exit')
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
                availables_sales_files = os.listdir('Python/Files/Sales')
                print('\n"Sales"')
                for element in availables_sales_files:
                    print(f'  - {element}')
                name_file = input('Enter the name file what you want to review (without .txt): ')
                if name_file == 'exit' or name_file == 'Exit':
                    sales_Manager()
                else:
                    try:
                        sales_file = open(f'Python/Files/Sales/{name_file}.txt', 'r+')
                        print(sales_file.read())
                        sales_file.close()
                        consult()
                    except:
                        print(f'The file "{name_file}" does not exist')
                
            if review_file == 2:
                availables_inventories_files = os.listdir('Python/Files/Inventories')
                print('"Inventories"')
                for element in availables_inventories_files:
                    print(f'  - {element}')
                name_file = input('Enter the name file what you want to review (without .txt): ')
                if name_file == 'exit' or name_file == 'Exit':
                    sales_Manager()
                else:
                    try:
                        sales_file = open(f'Python/Files/Inventories/{name_file}.txt', 'r+')
                        print(sales_file.read())
                        sales_file.close()
                        consult()
                    except:
                        print(f'The file "{name_file}" does not exist')
        except:
            print('"Answer error": Please select any to options availables')
            consult()
        
def available_Files():
    available_sales_files = os.listdir('Python/Files/Sales')
    available_inventory_files = os.listdir('Python/Files/Inventories')
    if len(available_sales_files) == 0 and len(available_inventory_files) == 0:
        print('"There are not any files in existence"')
    else:
        sales_inventories = available_sales_files + available_inventory_files
        for element in sales_inventories:
            print(f'- {element}')
            
    sales_Manager()
    
def update_data():
    print('Are you sure you want update the information?\n 1.- Yes\n 2.- No\n 3.- Exit')
    choice_update = input('Enter the desired option: ')
    print('\n')
    
    if choice_update == '3' or choice_update == 'Exit' or choice_update == 'exit':
        print('Leaving...')
        sales_Manager()
    else: 
        try:
            choice_update = int(choice_update)
            if choice_update <= 0 or choice_update >= 4:
                print('Answer error. Select 1 or 2\n')
                update_data()
        except:
            print('"The answer can only be 1 or 2"\n')
            update_data()
            
    if choice_update == 1:
        print('What do you want update?\n 1.- Sales\n 2.- Inventories')
        choice_update = input('Enter your answer: ')
        
        try:
            choice_update = int(choice_update)
            while choice_update <= 0 or choice_update >= 3:
                print('"The answer can only be 1 or 2"\n')
                choice_update = int(input('Enter your answer: '))
        except:
            print('"Answer error". Please enter 1 or 2\n')
            update_data()
        
        if choice_update == 1:
            availables_files = os.listdir('Python/Files/Sales')
            print("*** Availables Sales ***")
            count_files = 0
            for element in availables_files:
                count_files += 1
                print(f' {count_files}.- {element}')
            name_file = input('Enter the name file what you want update: ')
            try:
                sale_file = open(f'Python/Files/Sales/{name_file}.txt', 'r+')
                list_sale = []
                count_elements = 0
                for element in sale_file:
                    element = element[:-1]
                    list_sale.append(element)
                    count_elements += 1
                    print(f'{count_elements}.- {element}')
                choice = int(input('Enter the sale number what you want update: '))
                choice = choice - 1
                print('Enter the new information')
                next_icon = '->'
                product = input('Product: ')
                amount = int(input('Quantity: '))
                unit_price = float(input('Unit Price: $'))
                total_sale = unit_price * amount
                new_information = f'[Product: {product.capitalize()}] {next_icon} [Amount: {amount}] {next_icon} [Unit Price: ${unit_price}] {next_icon} [Total: ${total_sale}]'
                old_information = list_sale[choice]
                list_sale[choice] = new_information
                change = f'* Old information: {old_information}\n* New information: {new_information}'
                print(change)
                sale_file = open(f'Python/Files/Sales/{name_file}.txt', 'w')
                while len(list_sale) != 0:
                    first_value = list_sale.pop(0)
                    sale_file.write(f'{first_value}\n')
                sale_file = open(f'Python/Files/Sales/{name_file}.txt', 'r+')
                print('"Changes successfully completed"')
                print(sale_file.read())
                sale_file.close()
            except:
                print(f'The file {name_file} does not exist')
                update_data()
                
        elif choice_update == 2:
            availables_files = os.listdir('Python/Files/Inventories')
            print("*** Availables Inventories ***")
            count_files = 0
            for element in availables_files:
                count_files += 1
                print(f' {count_files}.- {element}')
            name_file = input('Enter the name file what you want update: ')
            try:
                stock_file = open(f'Python/Files/Inventories/{name_file}.txt', 'r+')
                list_stock = []
                count_elements = 0
                for element in stock_file:
                    element = element[:-1]
                    list_stock.append(element)
                    count_elements += 1
                    print(f'{count_elements}.- {element}')
                choice = int(input('Enter the inventory number what you want update: '))
                choice = choice - 1
                print('Enter the new information')
                product = input('Product: ')
                pieces = int(input('Quantity: '))
                new_information = f'{product.capitalize()} - {pieces} pzas/paq'
                old_information = list_stock[choice]
                list_stock[choice] = new_information
                change = f'* Old information: {old_information}\n* New information: {new_information}'
                print(change)
                stock_file = open(f'Python/Files/Inventories/{name_file}.txt', 'w')
                while len(list_stock) != 0:
                    list_stock.sort()
                    first_value = list_stock.pop(0)
                    stock_file.write(f'{first_value}\n')
                stock_file = open(f'Python/Files/Inventories/{name_file}.txt', 'r+')
                print('"Changes successfully completed"')
                print(stock_file.read())
                stock_file.close()
            except:
                print(f'The file {name_file} does not exist')
                update_data()
                
    elif choice_update == 3:
        print('Leaving...')
        sales_Manager()
    
def remove_data():
    print('Are you sure you want delete information?\n 1.- Yes\n 2.- No\n 3.- Exit')
    choice_remove = input('Enter the desired option: ')
    
    if choice_remove == '3' or choice_remove == 'Exit' or choice_remove == 'exit':
        print('Leaving...')
        sales_Manager()
    else: 
        try:
            choice_remove = int(choice_remove)
            if choice_remove <= 0 or choice_remove >= 4:
                print('Answer error. Select 1 or 2\n')
                remove_data()
        except:
            print('"The answer just can be 1 or 2"\n')
            remove_data()
            
    if choice_remove == 1:
        print('What do you want remove?\n 1.- Sales\n 2.- Prodcut(s)')
        choice_update = input('Enter your answer: ')
        
        try:
            choice_remove = int(choice_update)
            while choice_remove <= 0 or choice_remove >= 3:
                print('"The answer can only be 1 or 2"\n')
                choice_update = int(input('Enter your answer: '))
        except:
            print('"Answer error". Please enter 1 or 2\n')
            update_data()
            
        if choice_remove == 1:
            availables_files = os.listdir('Python/Files/Sales')
            print("*** Availables Sales ***")
            count_files = 0
            for element in availables_files:
                count_files += 1
                print(f' {count_files}.- {element}')
            name_file = input('Enter the name file: ')
            sale_file = open(f'Python/Files/Sales/{name_file}.txt', 'r+')
            list_sale = []
            count_elements = 0
            for element in sale_file:
                element = element[:-1]
                list_sale.append(element)
                count_elements += 1
                print(f'{count_elements}.- {element}')
            choice = int(input('Enter the sale you want to remove: '))
            choice = choice - 1
            del list_sale[choice]
            print(list_sale)
            sale_file = open(f'Python/Files/Sales/{name_file}.txt', 'w')
            while len(list_sale) != 0:
                first_value = list_sale.pop(0)
                sale_file.write(f'{first_value}\n')
            sale_file = open(f'Python/Files/Sales/{name_file}.txt', 'r+')
            print('\n"The sale has been removed"')
            sale_file.close()
        
        if choice_remove == 2:
            availables_files = os.listdir('Python/Files/Inventories')
            print("*** Availables Inventories ***")
            count_files = 0
            for element in availables_files:
                count_files += 1
                print(f' {count_files}.- {element}')
            name_file = input('Enter the name file: ')
            stock_file = open(f'Python/Files/Inventories/{name_file}.txt', 'r+')
            list_stock = []
            count_elements = 0
            for element in stock_file:
                element = element[:-1]
                list_stock.append(element)
                count_elements += 1
                print(f'{count_elements}.- {element}')
            choice = int(input('Enter the product you want to remove: '))
            choice = choice - 1
            del list_stock[choice]
            print(list_stock)
            stock_file = open(f'Python/Files/Inventories/{name_file}.txt', 'w')
            while len(list_stock) != 0:
                first_value = list_stock.pop(0)
                stock_file.write(f'{first_value}\n')
            stock_file = open(f'Python/Files/Inventories/{name_file}.txt', 'r+')
            print('\n"The product has been removed"')
            stock_file.close()
        
# Main function call
sales_Manager()