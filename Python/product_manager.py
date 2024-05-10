
##############################################################################################################################################################################################################################
class PRODUCT:     #* Clase para craear los prodcutos con sus propiedades
    def __init__(self, name, quantity, price, importt = 0):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.importt = importt
##############################################################################################################################################################################################################################
class Product_NUMBER:   #* Esta clase gestiona un diccionario para manejar los productos por orden numérico
    def __init__(self, products_list = [], new_product=None):
        self.products_list = products_list
        if new_product:
            self.add_product(new_product)
        from sale_manager import SALE_Manager
        self.class_sale = SALE_Manager()
##############################################################################################################################################################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def create_product(self):  #* Función general para crear los productos y para escribirlos en el archivo .txt (estoy pensado en separarlas)
        from file_manager import FILE_Manager
        self.class_file = FILE_Manager()  
        last_number = len(self.products_list)
        sale_number = last_number
        while True: #Loop es optener una respuesta deseada, con la cual poder continuar el proceso 
            self.class_sale.print_in_box(f"Adding product # {(sale_number)+1}")                                                                                       
            try:                                                                                       
                name = input("Description: ").capitalize() #Por lo pronto se permite cualquier tipo de caracter para el nombre (incluso espacio vacío, luego soluciono eso xd)
                quantity = int(input("Quantity sold: "))
                price = int(input("Price: $ "))
                self.class_sale.print_in_box("Product seccessfully added!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
            except:
                self.class_sale.print_in_box("ERROR: Only numbers must be typed for quantity and price!") #Reglas para el input (respuesta deseada)
                print("#########################################################".center(117))
            else:
                #################################################################
                importt = quantity * price
                new_product = PRODUCT(name, quantity, price, importt) #Se crea el objeto(PRODUCT) con sus propiedades definidas
                self.add_product(new_product)   #Se llama la funcion para agregar los productos
                sale_number += 1
                while True:     #Este loop es para continuar agregando productos o detenerse            
                    try:
                        print("--------------------------------------------------------------------------------------------------------------------")
                        answer = int(input("|               Would you like adding another product? (Type: 1 to continue or  2 to finish)               |---->  "))
                        print("--------------------------------------------------------------------------------------------------------------------\n")
                    except:
                        print("")
                        self.print_in_box("ERROR: Please, enter just 1 or 2!")
                        print("#################################".center(117))
                    else:
                        if answer == 1: 
                                ##Si se selecciona 1 (continuar) solo se detiene el loop interior (que es el que pregunta si se desea continuar o no)
                            break #Y continua con el loop exterior que es el que agrega los productos
                        if answer == 2:   
                            break #Si de desea parar y no agregar mas productos se detiene el loop interior y posteriormente el loop exterior hace break tambien
                if answer == 2:
                    self.class_file.write_in_txt(self.products_list)
                    self.class_file.consult() #consult te saca al menu de navegacion
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                    break
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def add_product(self, new_product):   #* Esta función agrega los productos al dict (comenzando con el indice 1 para que coincida con nuestra forma de contar) 
        self.products_list.append(new_product)  #Posteriormente en la clase Sales_manage en la función create_product se asocia el indice con la variable sale_number
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def get_product(self, number_by_user):   #*Esta función es para obtener un producto determinado (por numero de producto)
        if number_by_user < 1 or number_by_user > len(self.products_list):
            return None
        return self.products_list[number_by_user - 1]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def change_product_info(self):    #* Funcion para cambiar datos del prodcuto seleccionado (ya sea nombre, cantidad o precio)
        from sale_manager import SALE_Manager
        self.class_sale = SALE_Manager()   #*Instancia para llamar a la clase SALE_Manager() y sus funciones dentro de esta funcion
        from file_manager import FILE_Manager
        self.class_file = FILE_Manager()
        if self.products_list:
            while True:   #Bucle para verificar que el numero de producto realmente exista
                try:
                    self.class_sale.print_in_box("----------> Please, enter # of the product to modify <----------")
                    self.class_sale.print_in_box("Enter 0 to exit")
                    number_by_user = int(input("---------------------------------------------------------->: "))
                    print("")
                    if number_by_user == 0:
                        self.class_file.consult()
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                        break
                    else:
                        #Se llama a la funcion get_product() que es la que se encarga de buscar un producto por numero y lo retorna quedando disponible del producto para hacer modificaciones 
                        current_product = self.get_product(number_by_user)
                        if current_product:     #Si el producto existe se procede con el siguiente paso, si no se vuelve a solicitar
                            while True:          #Bucle para verificar que se ingrese una opcion valida
                                try:      
                                    print("---------------------------------------------------------------------------------------------------------------------")
                                    print("|                                            What do you need to change?                                            |")
                                    print("|                                              1: Product Description                                               |")
                                    print("|                                                 2: Quantity sold                                                  |")   #*Chingona la piramide no? xd
                                    print("|                                                     3:  Price                                                     |")
                                    print("|                                                         ;)                                                        |")
                                    print("---------------------------------------------------------------------------------------------------------------------\n")
                                    change = int(input("---------------- Enter the number of your selection --->: ")) 
                                    print("")
                                    if change == 1 :
                                        new_name = input("-------------------------->Enter new product description: ").capitalize()
                                        print("")
                                        current_product.name = new_name 
                                        self.class_file.write_in_txt(self.products_list)
                                        self.class_sale.print_in_box ("|||||  Description updated!  |||||")
                                        print("~~~~~~~~~~~~~~~~~~~~".center(117))
                                        break
                                    elif change == 2:                           # creo estos bucles no requieren mayor explicacion
                                        while True:                             # estan en busca de la respuesta apropiada
                                            try:
                                                new_quantity = int(input("-------------------------------->Enter new quantity sold: "))
                                                print("")
                                            except:
                                                print("")
                                                self.class_sale.print_in_box("ERROR: Please, enter a valid quantity (just numbers, any other caracter)")
                                                print("########################################################################".center(117))
                                            else:
                                                current_product.quantity = new_quantity
                                                current_product.importt = current_product.quantity * current_product.price
                                                self.class_file.write_in_txt(self.products_list)
                                                self.class_sale.print_in_box ("|||||  Quantity updated!  |||||")
                                                print("~~~~~~~~~~~~~~~~~".center(117))
                                                break
                                    elif change == 3 :
                                        while True:
                                            try:
                                                self.class_sale.print_in_box(" Enter new price (Just number, no dollar sign)")                                             
                                                new_price = int(input("(----------------------------------------------------> :$ "))
                                                print("")
                                            except: 
                                                print("")
                                                self.class_sale.print_in_box("Please, enter a valid new price (just numbers, any other caracter)")
                                                print("##################################################################".center(117))
                                            else:    
                                                current_product.price = new_price
                                                current_product.importt = current_product.quantity * current_product.price
                                                self.class_sale.print_in_box ("|||||  Price updated!  |||||")
                                                print("~~~~~~~~~~~~~~".center(117))
                                                self.class_file.write_in_txt(self.products_list)
                                                break
                                    elif change < 1 or change > 3:
                                        self.class_sale.print_in_box("ERROR: Please, enter a valid selection number (1, 2 or 3)!")
                                        print("##########################################################".center(117))
                                    break #* Este break es para finalizar el bucle intermedio y volver a preguntar que producto se desea modificar si es el caso, o salir si se ha terminano

                                except:
                                    print("")
                                    self.class_sale.print_in_box("ERROR: Please, enter a selection number! (not any other caracter)")
                                    print("#################################################################".center(117))
                            
                        else:
                            self.class_sale.print_in_box("ERROR: That product # doesn´t exist!... Please try again ;)") #Si el numero de producto ingresado no existe se notifica al usuario y se repite el bucle
                            print("###########################################################".center(117))

                except:
                    print("")
                    self.class_sale.print_in_box("ERROR: Please, enter a PRODUCT # only, not any other caracter!")
                    print("##############################################################".center(117))
        else:
            self.class_sale.print_in_box("There´s no products added yet!, to add products enter 1.")
            print("#########################################################".center(117))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def remove_product (self):    #* Función para remover un producto (por #)
        from sale_manager import SALE_Manager
        self.class_sale = SALE_Manager()   #*Instancia para llamar a la clase SALE_Manager() y sus funciones dentro de esta clase principal
        from file_manager import FILE_Manager
        self.class_file = FILE_Manager()
        if self.products_list:
            while True:      #Igual que los anteriores loop de verificacion
                try:
                    if self.products_list:
                        self.class_sale.print_in_box("----------> Please enter # of the product to remove <----------")
                        self.class_sale.print_in_box("Enter 0 to exit")
                        number_by_user=int(input("--------------------------------------------------------> #: "))
                        print("")
                        if number_by_user == 0:
                            self.class_file.consult()
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                            break #Se rompe el loop una vez teminado el proceso
                        
                    else:
                        self.class_sale.print_in_box("|||||  There's no more products!  |||||")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                        break
                except:
                    print("")
                    self.class_sale.print_in_box("ERROR: Please enter just the product number to remove!")
                    print("######################################################".center(117))
                else:
                    product_to_remove = self.get_product(number_by_user)
                    if product_to_remove:
                        self.products_list.remove(product_to_remove)    #Si el numero de producto dado por el usuario existe se elimina
                        self.class_sale.print_in_box("|||||  Product deleted!  |||||")
                        print("~~~~~~~~~~~~~~~~".center(117))
                        self.class_file.write_in_txt(self.products_list)
                    else:
                        self.class_sale.print_in_box("ERROR: That product # doesn´t exist!... Please try again ;)")
                        print("###########################################################".center(117))
        else:
            self.class_sale.print_in_box("There´s no products added yet!, to add products select option 1.")
            print("################################################################".center(117))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
