from product_manager import Product_NUMBER, PRODUCT

##############################################################################################################################################################################################################################
class SALE_Manager:     #*Clase principal para gestionar el programa
    def __init__(self,last_number=0):
        self.last_number = last_number  #* En esta propiedad se guarda el # del ultimo producto agregado y se actuliza al finalizar la funcion creat_product()
        self.class_number =Product_NUMBER()   #*Instancia para llamar a la clase Sale_number() y sus funciones dentro de esta clase principal
        self.print_in_box("You´re in SALES management, let´s begin adding products...")
        self.create_product() #Se inicia el programa con la obligacion de agregar al menos un producto
##############################################################################################################################################################################################################################
    def navigation(self): #* Nombre autodescriptivo xd 
        print("---------------------------------------------------------------------------------------------------------------------")
        print("|                                              What do you need to do?                                              |")
        print("|                    1: To change any product information (Description, Quantity sold  or Price)                    |")
        print("|                                             2: To remove any product                                              |")
        print("|                                         3: To consult all sale´s products                                         |")
        print("|                                                4: To add products                                                 |")
        print("|                                            5: To get sale´s total                                                 |")
        print("---------------------------------------------------------------------------------------------------------------------\n")
        while True:
            try:
                response=int(input("To continue, please type the number of your selection ----> "))
                print("")
            except:
                print("")
                self.print_in_box("-----> Only numbers must be typed for a valid selection <-----")
                print("")
            else:
                if response < 1 or response > 5:
                    print("")
                    self.print_in_box("-----> Please, enter a valid selection number <-----")
                    print("")
                elif response == 1:
                    self.change_product_info()
                elif response == 2:
                    self.remove_product()
                elif response == 3:
                    self.consult()
                elif response == 4:
                    self.create_product(self.last_number)
                elif response == 5:
                    self.sale_calculation()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def print_in_box(self,message, min_length = 113): #* Funcion para imprimir con formato en consola)
        length = max(len(message), min_length)     #-------------------------------------------------------------------------------------
        print("-" * (length + 4))                  #|             Formato de CAJA que centra el contenido automaticamente               |
        print("|", message.center(length), "|")    #-------------------------------------------------------------------------------------
        print("-" * (length + 4))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def create_product(self,last_number=0):  #* Función general para crear los productos y para escribirlos en el archivo .txt (estoy pensado en separarlas)
        from file_manager import FILE_Manager  # Importación local para evitar el problema de importación circular
        self.class_file = FILE_Manager()  # Instancia de FILE_Manager para escribir en el archivo
        current_number = last_number    #La variable sale_number se actualiza con last_number que contine el # del último producto agregado, en caso de ser el primero o haber eliminado todos los productos es igual a cero por defecto                                                                                                                   
        while True: #Loop es optener una respuesta deseada, con la cual poder continuar el proceso 
            self.print_in_box(f"Product # {(current_number)+1}")                                                                                       
            try:                                                                                       
                name = input("Description: ").capitalize() #Por lo pronto se permite cualquier tipo de caracter para el nombre (incluso espacio vacío, luego soluciono eso xd)
                quantity = int(input("Quantity sold: "))
                price = int(input("Price: "))
            except:
                print("")
                self.print_in_box("-----> Only numbers must be typed for quantity and price <-----") #Reglas para el input (respuesta deseada)
                print("")
            else:
                importt = quantity * price
                new_product = PRODUCT(name, quantity, price, importt) #Se crea el objeto(PRODUCT) con sus propiedades definidas
                self.class_number.add_product(new_product)   #Se llama la funcion para agregar los productos
                current_number += 1
                while True:     #Este loop es para continuar agregando productos o detenerse            
                    try:
                        print("--------------------------------------------------------------------------------------------------------------------")
                        answer = int(input("|               Would you like adding another product? (Type: 1 to continue or  2 to finish)               |---->  "))
                        print("--------------------------------------------------------------------------------------------------------------------\n")
                    except:
                        print("")
                        self.print_in_box("-----> Please enter just 1 or 2 <-----")
                        print("")
                    else: 
                        if answer == 1:                                                              
                                #Si se selecciona 1 (continuar) solo se detiene el loop interior (que es el que pregunta si se desea continuar o no)
                            break #Y continua con el loop exterior que es el que agrega los productos
                        if answer == 2:                                                                 
                            break #Si de desea parar y no agregar mas productos se detiene el loop interior y posteriormente el loop exterior hace break tambien
                        else:
                            print("")
                            self.print_in_box("-----> Please enter just 1 or 2 <-----")
                            print("")
                if answer == 2: #Se detiene tambien el loop exterior dando seguimiento a la condicional (if answer == 2: del loop interior)
                    break   #Se detiene tambien el loop exterior dando seguimiento a la condicional (if answer == 2: del loop interior)
        self.last_number = current_number       #* Aquí se actualiza el # del último producto agregado una vez terminado el loop de creacion de productos
        self.class_number.update_products()
        self.class_file.write_products_in_txt()
        self.class_file.print_total_in_txt()
        self.consult()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def consult(self): #* Funcion simple para consultar todos los productos (planeo agregar la opcion para consultar por numero o nombre de producto)
        if self.class_number.get_product(1):
            with open("C:/Python/Files/Sales/current_sale.txt", "r") as fileee:
                for line in fileee:
                    print(line.strip())
            print("")
        else:
            self.print_in_box("There´s no products added")
            print("")
        self.navigation()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SALE_Manager()