
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
        #*Se declara la lista como predeterminada para eviatar que con cada llamado el constructor la inicialice  y se borren los productos previamente agregados
        self.products_list = products_list
        from sale_manager import SALE_Manager
        self.class_sale = SALE_Manager() #Instancia para llamar funciones de SALE_Manager() 
##############################################################################################################################################################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def create_product(self):  #* Función para crear los productos (tambien llama a la funcion write_in_txt() para escribirlos en el archivo)
        from file_manager import FILE_Manager
        self.class_file = FILE_Manager()  #Instancia para llamar funciones de FILE_Manager
        last_number = len(self.products_list) #variable para llevar un conteo de productos agregados y mostrar el numero de producto que se esta agregando durante el proceso
        current_number = last_number #current number es el numero actual de producto que se encuentra en proceso de creacion
        while True: #Loop es optener una respuesta deseada, con la cual poder continuar el proceso adecuadamente 
            self.class_sale.print_in_box(f"Adding product # {(current_number)+1}") #mensaje para notificar al usuario el numero de producto que se encuentra agregando                                                                                      
            try:                                                                                       
                name = input("Description: ").capitalize() #Por lo pronto se permite cualquier tipo de caracter para el nombre
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
                new_product = PRODUCT(name, quantity, price, importt) #Se crea el objeto (PRODUCT) con sus propiedades definidas por los inputs del usuario
                self.add_product(new_product)   #Se llama la funcion para agregar los productos a la lista
                current_number += 1 #se actualiza el conteo 
                while True: #loop para continuar agregando productos o detenerse segun inidque el usuario          
                    try:
                        print("--------------------------------------------------------------------------------------------------------------------")
                        answer = int(input("|               Would you like adding another product? (Type: 1 to continue or  2 to finish)               |---->  "))
                        print("--------------------------------------------------------------------------------------------------------------------\n")
                    except:
                        print("")
                        self.class_sale.print_in_box("ERROR: Please, enter just 1 or 2!")
                        print("#################################".center(117))
                    else:
                        if answer == 1: 
                                ##Si se selecciona 1 (continuar) solo se detiene el loop interior (que es el que pregunta si se desea continuar o no)
                            break #Y continua con el loop exterior que es el que agrega los productos
                        elif answer == 2:   
                            break #Si de desea parar y no agregar mas productos se detiene el loop interior y posteriormente el loop exterior hace break tambien
                        else:
                            self.class_sale.print_in_box("ERROR: Please, just 1 to continue or 2 to exit!")
                            print("###############################################".center(117))
                        
                if answer == 2: #al detenerse el proceso para agregar productos...
                    self.class_file.write_in_txt(self.products_list) #se llama a la funcion para escribir el txt pasandole la lista de productos
                    self.class_file.consult() #se llama a la funcion para mostrar los productos ingresados al usuario
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                    break #loop exterior hace break para dar continuidad a la seleccion del usuario 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def add_product(self, new_product):   #* Esta función agrega los productos a la lista de productos
        self.products_list.append(new_product) 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def get_product(self, number_by_user):   #*Esta función es para obtener un producto determinado (por numero de producto)
        if number_by_user < 1 or number_by_user > len(self.products_list):
            #si el numero de producto dado por el usuario no existe (menor que 1 o mayor que la longitud de la lista)
            return None #se retorna None
        #pero si el numero dado por el usuario existe:
        return self.products_list[number_by_user - 1]  
        #se retorna el producto del indice calculado por: el numero dado por el usuario, menos uno. Ya que es el correspondiente debido al indice 0 en las listas
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def change_product_info(self):    #* Funcion para cambiar datos del prodcuto seleccionado (ya sea nombre, cantidad o precio)
        from sale_manager import SALE_Manager
        self.class_sale = SALE_Manager()   #Instancia para llamar funciones de SALE_Manager() 
        from file_manager import FILE_Manager
        self.class_file = FILE_Manager() #Instancia para llamar funciones de FILE_Manager()
        if self.products_list: ###* Condicional para verificar si existen productos en la lista y posterioirmente proceder con la ejecucion de la funcion
            while True:   #Bucle para verificar que el numero de producto realmente exista
                try:
                    self.class_sale.print_in_box("----------> Please, enter # of the product to MODIFY <----------")
                    self.class_sale.print_in_box("Enter 0 to exit")
                    number_by_user = int(input("---------------------------------------------------------->: "))
                    print("")
                    if number_by_user == 0:
                        self.class_file.consult()
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                        break
                    else:
                        #Se llama a la funcion get_product() que es la que se encarga de buscar un producto por numero y retonando el producto indicado por el usuario en caso de existir
                        current_product = self.get_product(number_by_user) #*Se crea la variable para acceder a las propiedades de cada producto (indicado por el usuario)
                        if current_product:     #Si el producto existe se procede con el siguiente paso, si no se vuelve a solicitar
                            while True:   #loop para verificar que se ingrese una opcion valida
                                try:      
                                    print("---------------------------------------------------------------------------------------------------------------------")
                                    print("|                                                  Enter 0 to exit                                                  |")
                                    print("|                                                                                                                   |")
                                    print("|                                            What do you need to change?                                            |")
                                    print("|                                              1: Product Description                                               |")
                                    print("|                                                 2: Quantity sold                                                  |")   #*Chingona la piramide no? xd
                                    print("|                                                     3:  Price                                                     |")
                                    print("|                                                         ;)                                                        |")
                                    print("---------------------------------------------------------------------------------------------------------------------\n")
                                    change = int(input("---------------- Enter the number of your selection --->: ")) 
                                    print("")
                                    if change == 0:
                                        break
                                    elif change == 1 :
                                        new_name = input("-------------------------->Enter new product description: ").capitalize()
                                        print("")
                                        current_product.name = new_name   #Se accede y actualiza la propiedad name del producto (que es la que contiene la descripcion del mismo)
                                        #Se llama a la funcion encargada de escribir la info en el txt para actualizarlo tambien (conforme la reciente modificacion al producto (propiedad name))
                                        self.class_file.write_in_txt(self.products_list) #y se le pasa la lista de productos para que lleve a cabo el proceso 
                                        self.class_sale.print_in_box ("|||||  Description updated!  |||||")
                                        print("~~~~~~~~~~~~~~~~~~~~".center(117))
                                    elif change == 2:  #Creo que los siguientes loops no requieren mayor explicacion, estan en busca de la respuesta apropiada
                                        while True:    
                                            try:
                                                new_quantity = int(input("-------------------------------->Enter new quantity sold: "))
                                                print("")
                                            except:
                                                print("")
                                                self.class_sale.print_in_box("ERROR: Please, enter a valid quantity (just numbers,not any other caracter)")
                                                print("########################################################################".center(117))
                                                print("")
                                            else:
                                                current_product.quantity = new_quantity #Se accede y actualiza la propiedad quantity del producto
                                                #aqui se recalcula el importe basado en la modificacion que se acaba de realizar al producto
                                                current_product.importt = current_product.quantity * current_product.price 
                                                self.class_file.write_in_txt(self.products_list) #Se llama a la funcion encargada de escribir la info en el txt
                                                self.class_sale.print_in_box ("|||||  Quantity updated!  |||||")
                                                print("~~~~~~~~~~~~~~~~~".center(117))
                                                break #para finalizar el loop en busca de un input valido
                                    elif change == 3 :
                                        while True:
                                            try:
                                                self.class_sale.print_in_box(" Enter new price (Just number, no dollar sign)")                                             
                                                new_price = int(input("(----------------------------------------------------> :$ "))
                                                print("")
                                            except: 
                                                print("")
                                                self.class_sale.print_in_box("Please, enter a valid new price (just numbers, not any other caracter)")
                                                print("##################################################################".center(117))
                                                print("")
                                            else:    
                                                current_product.price = new_price #Se accede y actualiza la propiedad price del producto
                                                #se recalcula el importe basado en la modificacion que se acaba de realizar al producto
                                                current_product.importt = current_product.quantity * current_product.price 
                                                self.class_sale.print_in_box ("|||||  Price updated!  |||||")
                                                print("~~~~~~~~~~~~~~".center(117))
                                                self.class_file.write_in_txt(self.products_list) #Se llama a la funcion encargada de escribir la info en el txt
                                                break #para finalizar el loop en busca de un input valido
                                    elif change < 1 or change > 3:
                                        self.class_sale.print_in_box("ERROR: Please, enter a valid selection number (1, 2 or 3)!")
                                        print("##########################################################".center(117))

                                except:
                                    print("")
                                    self.class_sale.print_in_box("ERROR: Please, enter a selection number! (not any other caracter)")
                                    print("#################################################################".center(117))
                            
                        else:
                            self.class_sale.print_in_box("ERROR: That product # doesn´t exist!... Please try again ;)") 
                            print("###########################################################".center(117))

                except:
                    print("")
                    self.class_sale.print_in_box("ERROR: Please, enter a PRODUCT # only, not any other caracter!")
                    print("##############################################################".center(117))
        else:
            #* Mensaje para notificar si aun no hay productos agregados antes de ejecutar el resto del proceso
            self.class_sale.print_in_box("There´s no products added yet!, to add products select option 1.")
            #* la funcion termina aqui y se devuelve al loop infinito de navigation()
            print("#########################################################".center(117))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def remove_product (self):    #* Función para remover un producto (por #)
        from sale_manager import SALE_Manager
        self.class_sale = SALE_Manager()   #*Instancia para llamar funciones de SALE_Manager()
        from file_manager import FILE_Manager
        self.class_file = FILE_Manager()
        if self.products_list: ###* Condicional para verificar si existen productos en la lista y posterioirmente proceder con la ejecucion de la funcion
            while True: #Igual que los anteriores loop: de verificacion
                try:
                    if self.products_list: ###* Segunda condicional para verificar si aun existen productos en la lista (posterior a una eliminacion)
                        self.class_sale.print_in_box("----------> Please enter # of the product to remove <----------")
                        self.class_sale.print_in_box("Enter 0 to exit")
                        number_by_user=int(input("--------------------------------------------------------> #: "))
                        print("")
                        if number_by_user == 0:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                            break #Se rompe este loop y en automatico se vuelve a loop de navigation()
                        
                    else: #* Y si no hay mas productos despues de un proceso de eliminacion notificarlo al usuario 
                        self.class_sale.print_in_box("|||||  There's no more products!  |||||")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~".center(117))
                        break #* Se termina la ejecucion y en automatico se devuelve al loop de navigation()
                except:
                    print("")
                    self.class_sale.print_in_box("ERROR: Please enter just the product number to remove!")
                    print("######################################################".center(117))
                else:
                    product_to_remove = self.get_product(number_by_user) #* Se crea la variable para ejecutar la funcion del sistema .remove()
                    if product_to_remove: # Si el numero dado por el usuario existe:
                        self.products_list.remove(product_to_remove)  #Se elimina
                        self.class_sale.print_in_box("|||||  Product deleted!  |||||")
                        print("~~~~~~~~~~~~~~~~".center(117))
                        self.class_file.write_in_txt(self.products_list) # Y se actualiza el txt 
                        self.class_file.consult()
                    else:
                        self.class_sale.print_in_box("ERROR: That product # doesn´t exist!... Please try again ;)")
                        print("###########################################################".center(117))
        else:
            #* Mensaje para notificar si aun no hay productos agregados antes de ejecutar el resto del proceso
            self.class_sale.print_in_box("There´s no products added yet!, to add products select option 1.")
            #* la funcion termina aqui y se devuelve al loop de navigation()
            print("################################################################".center(117))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
