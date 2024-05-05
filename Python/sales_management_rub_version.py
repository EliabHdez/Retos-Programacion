""" 
    EJERCICIO: 
    - Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
    - Cada producto se guarda en una línea del archivo de la siguiente manera: [nombre_producto], [cantidad_vendida], [precio].
    - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
    - También debe poseer opciones para calcular la venta total y por producto.
    - La opción salir borra el .txt.
"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
fileee=open("C:/Python/Files/Sales/current_sale.txt", "w+")   #* Recien se ejecuta el programa se crea el archivo .txt sobre el cual se trabajará
##############################################################################################################################################################################################################################
class PRODUCT:     #* Clase para craear los prodcutos con sus propiedades
    def __init__(self, name, quantity, price, importt = 0):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.importt = importt
##############################################################################################################################################################################################################################
class Sale_number:   #* Esta clase gestiona un diccionario para manejar los productos por orden numérico
    def __init__(self,new_product=None):
        self.products_dict = {}
        if new_product:
            self.add_product(new_product)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def add_product(self, new_product):   #* Esta función agrega los productos al dict (comenzando con el indice 1 para que coincida con nuestra forma de contar) 
        self.products_dict[len(self.products_dict) + 1] = new_product  #Posteriormente en la clase Sales_manage en la función create_product se asocia el indice con la variable sale_number
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def get_product(self, number_by_user):   #*Esta función es para obtener un producto determinado (por numero de producto)
        return self.products_dict.get(number_by_user)
    
##############################################################################################################################################################################################################################
class Sales_manage:     #*Clase principal para gestionar el programa
    def __init__(self,last_number=0):
        self.last_number = last_number  #* En esta propiedad se guarda el # del ultimo producto agregado
        self.clas_sale_number = Sale_number()   #*Instancia para llamar a la clase Sale_number() y sus funciones dentro de esta clase principal
        self.print_in_box("You´re in SALES management, let´s begin adding products...")
        self.create_product() #Se inicia el programa con la obligacion de agregar al menos un producto
        self.navigation()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        sale_number = last_number    #La variable sale_number se actualiza con last_number que contine el # del último producto agregado, en caso de ser el primero o haber eliminado todos los productos es igual a cero por defecto                                                                 
        with open("C:/Python/Files/Sales/current_sale.txt", "a") as fileee:                                                    
            while True: #Loop es optener una respuesta deseada, con la cual poder continuar el proceso 
                self.print_in_box(f"Product # {(sale_number)+1}")                                                                                       
                try:                                                                                       
                    name = input("Description: ").capitalize() #Por lo pronto se permite cualquier tipo de caracter para el nombre (incluso espacio vacío, luego soluciono eso xd)
                    quantity = int(input("Quantity sold: "))
                    price = int(input("Price: "))
                except:
                    print("")
                    self.print_in_box("-----> Only numbers must be typed for quantity and price <-----") #Reglas para el input (respuesta deseada)
                    print("")
                else:
                    Number_symbol = "#: "         #Variable para dar formato al texto 
                    str_product = "Description: " #Variable para dar formato al texto 
                    str_qty = "Qty: "             #Variable para dar formato al texto 
                    str_price = "Price: "         #Variable para dar formato al texto 
                    dollar_sign = str("$ ")       #Variable para dar formato al texto
                    str_importt = "Import: "      #Variable para dar formato al texto
                    importt = quantity * price
                    new_product = PRODUCT(name, quantity, price, importt) #Se crea el objeto(PRODUCT) con sus propiedades definidas
                    self.clas_sale_number.add_product(new_product)   #Se llama la funcion para agregar los productos
                    sale_number += 1    
                    product_info=(f"|  {(str(Number_symbol)+str(sale_number)).center(4)}  |  {(str(str_product)+(name)).center(47)}  |  {(str(str_qty)+str(quantity)).center(10)}  |  {((str_price)+str(dollar_sign)+str(price)).center(15)}  |  {((str_importt)+str(dollar_sign)+str(importt)).center(15)}  |")
                    with open("C:/Python/Files/Sales/current_sale.txt", "a") as fileee:  #Se escribe todo ya formateado en el .txt (formato de tabla para una mayor facilidad de lectura de datos) 
                        fileee.write("-" * 117 + "\n")            #para que así se imprima en cosola (ese formato de tabla que viene desde el archivo .txt)
                        fileee.write(f"{product_info}\n")   
                        fileee.write("-" * 117 + "\n")
                    while True:     #Este loop es para continuar agregando productos o detenerse            
                        try:
                            print("--------------------------------------------------------------------------------------------------------------------")
                            answer = int(input("|               Would you like adding another product? (Type: 1 to continue or  2 to finish)               |---->  "))
                            print("--------------------------------------------------------------------------------------------------------------------\n")
                        except:
                            print("")
                            self.print_in_box(f"Please, enter just 1 or 2")
                            print("")
                        else: 
                            if answer == 1:                                                              
                                    ##Si se selecciona 1 (continuar) solo se detiene el loop interior (que es el que pregunta si se desea continuar o no)
                                break #Y continua con el loop exterior que es el que agrega los productos
                            if answer == 2:                                                                 
                                break #Si de desea parar y no agregar mas productos se detiene el loop interior y posteriormente el loop exterior hace break tambien
                            else:
                                self.print_in_box("-----> Please enter just 1 or 2 <-----")
                                print("")
                    if answer == 2: 
                            break   #Se detiene tambien el loop exterior dando seguimiento a la condicional (if answer == 2: del loop interior)
            total_sum=0
            for index, product in self.clas_sale_number.products_dict.items():
                product=self.clas_sale_number.get_product(index)
                total_sum+=(product.importt)
            str_total = "Total: "
            total_info = (f"|{(str(str_total)+str(total_sum)).center(115)}|")
            self.update_info()   #Con la funcion update_info borramos en el txt la info anterior (lo cual es necesario si es la segunda ves que se escribe despues de salir al menu de navegacion)
            with open("C:/Python/Files/Sales/current_sale.txt", "a") as fileee: #Ya que la primera vez que se sale, en automatico se escirbe al final el total en el txt y este quearía ahi si no se actualiza
                fileee.write("-" * 117 + "\n")
                fileee.write(f"{total_info}\n")
                fileee.write("-" * 117 + "\n")

        self.last_number=sale_number       #* Aquí se actualiza el # del último producto agregado
        self.consult()
        self.navigation()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def consult(self): #* Funcion simple para consultar todos los productos (planeo agregar la opcion para consultar por numero o nombre de producto)
        if self.clas_sale_number.get_product(1):
            with open("C:/Python/Files/Sales/current_sale.txt", "r") as fileee:
                for line in fileee:
                    print(line.strip())
            print("")
        else:
            self.print_in_box("There´s no products added")
            print("")
        self.navigation()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def change_product_info(self):    #* Funcion para cambiar datos del prodcuto seleccionado (ya sea nombre, cantidad o precio)
        while True:   #Bucle para verificar que el numero de producto realmente exista
            self.print_in_box("Please enter # of the product: ")
            try:
                number_by_user = int(input("------------------------->#: "))
                print("")

            except:
                print("")
                self.print_in_box("-----> Please, enter a PRODUCT # <-----")
                print("")
            else:
                #Se llama a la funcion get_product() que es la que se encarga de buscar un producto por numero y lo retorna quedando disponible del producto para hacer modificaciones 
                current_product = self.clas_sale_number.get_product(number_by_user)
                if current_product:     #Si el producto existe se procede con el siguiente paso, si no se vuelve a solicitar
                    while True:          #Bucle para verificar que se ingrese una opcion valida
                        try:      
                            print("---------------------------------------------------------------------------------------------------------------------")
                            print("|                                           What do you need to change?                                             |")
                            print("|                                             1: Product Description                                                |")
                            print("|                                                2: Quantity sold                                                   |")   #*Chingona la piramide no? xd
                            print("|                                                    3:  Price                                                      |")
                            print("|                                                        ;)                                                         |")
                            print("---------------------------------------------------------------------------------------------------------------------\n")
                            change = int(input("---------------------------------------- Enter the number of your selection ----------------------------------------> #: ")) 
                            print("")

                        except:
                            print("")
                            self.print_in_box("Please, enter just a valid selection number")
                            print("")
                        else:
                            if change == 1 :
                                new_name = input("Enter new product Description --->: ").capitalize()
                                print("")
                                current_product.name = new_name 
                                break
                            elif change == 2:                           # creo estos bucles no requieren mayor explicacion
                                while True:                             # estan en busca de la respuesta apropiada
                                    try:
                                        new_quantity = int(input("Enter new quantity sold --->: "))
                                        print("")
                                    except:
                                        print("")
                                        self.print_in_box("Please, enter a valid quantity")
                                        print("")
                                    else:
                                        current_product.quantity = new_quantity
                                        break
                            elif change == 3 :
                                while True:
                                    try:
                                        self.print_in_box(" Enter new price (Just number, no dollar sign)")                                             
                                        new_price = int(input("( ---> $: "))
                                        print("")
                                    except: 
                                        print("")
                                        self.print_in_box("Please, enter a valid new price")
                                        print("")
                                    else:    
                                        current_product.price = new_price
                                        break
                        if change < 1 or change > 3:
                            self.print_in_box("Please, enter a valid selection number")
                            print("")
                        
                        self.update_info()
                        self.consult()
                        self.navigation()
                else:
                    self.print_in_box("This product # doesn´t exist. ---> Please, try again...") #Si el numero de producto ingresado no existe se notifica al usuario y se repite el bucle
                    print("")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def remove_product (self):    #* Función para remover un producto (por #)
        while True:      #Igual que los anteriores loop de verificacion
            try:
                self.print_in_box("Please enter # of the product to remove: ")
                print("")
                number_by_user=int(input("---> #: "))
                print("")
            except:
                print("")
                self.print_in_box("-----> Please enter just a number <-----")
                print("")
            else:
                if number_by_user in self.clas_sale_number.products_dict:    #Si el numero de producto dado por el usuario existe:
                    del self.clas_sale_number.products_dict[number_by_user]  #El producto asosiaco a este se elimina del diccionario
                    self.print_in_box("-----> Product deleted <-----")
                    self.update_info()     #Se actualiza los datos
                    self.consult()  #Y se devuelve en automatico para el usuario una consulta de los productos 
                    break   #Se rompe el loop una vez teminado el proceso
                else:
                    self.print_in_box("-----> That sale # doesn´t exist... Please try again <-----")
                    print("")
        self.navigation()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def update_info(self):    #* Función para actualizar datos despues de realizar una modificacion, tanto del dict como del txt
        updated_products_dict = {}    #Diccionario (temporal) para almacenar los productos actualizados en el orden correcto
        for index, product in enumerate(self.clas_sale_number.products_dict.values(), start=1): #*Loop for para obtener los elementos del diccionario ya modificado, obteniendo values(el producto) comenzando por el indice 1 
            updated_products_dict[index]=product                                                #*Para reasignar el # de producto correctamente desde el índice 1 en el (dict temporal) y estecoindida con el numero de venta actualizado
                                                                                                #*ya que los items en products_dict quedaron desfasados debido a la eliminacion de un producto
        self.clas_sale_number.products_dict = updated_products_dict   #Se llama al diccionario modificado para actualizarlo con la informacion del diccionario temporal

        with open("C:/Python/Files/Sales/current_sale.txt", "w") as fileee:                 
            for index, product in self.clas_sale_number.products_dict.items():  #Loop-for para acceder a las propiedades de cada producto contenido en el dict ya actualizado, y a su vez actualizar los datos en el .txt
                Number_symbol = "#: "         #Variable para dar formato al texto 
                str_product = "Description: " #Variable para dar formato al texto 
                str_qty = "Qty: "             #Variable para dar formato al texto 
                str_price = "Price: "         #Variable para dar formato al texto 
                dollar_sign = str("$ ")       #Variable para dar formato al texto
                str_importt = "Import: "      #Variable para dar formato al texto
                product_info = f"|  {(str(Number_symbol)+str(index)).center(4)}  |  {(str(str_product)+(product.name)).center(47)}  |  {(str(str_qty)+str(product.quantity)).center(10)}  |  {((str_price)+str(dollar_sign)+str(product.price)).center(15)}  |  {((str_importt)+str(dollar_sign)+str(product.importt)).center(15)}  |"
                fileee.write("-" * 117 + "\n")                                                   
                fileee.write(f"{product_info}\n")  #Se escribe la info con formato de tabla en el .txt                                
                fileee.write("-" * 117 + "\n")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def sale_calculation(self):
        total_sum=0
        for index, product in self.clas_sale_number.products_dict.items() :
            product=self.clas_sale_number.get_product(index)
            total_sum+=(product.importt)
        self.print_in_box(f"Total import: ${total_sum}")
        print("")
        self.navigation()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Sales_manage()  #Inicia el programa
