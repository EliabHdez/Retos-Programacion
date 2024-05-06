
import file_manager
##############################################################################################################################################################################################################################
class PRODUCT:     #* Clase para craear los prodcutos con sus propiedades
    def __init__(self, name, quantity, price, importt = 0):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.importt = importt
##############################################################################################################################################################################################################################
class Product_NUMBER:   #* Esta clase gestiona un diccionario para manejar los productos por orden numérico
    def __init__(self,new_product=None):
        self.class_file = file_manager.FILE_Manager()
        self.products_dict = {}
        if new_product:
            self.add_product(new_product)
##############################################################################################################################################################################################################################
    def add_product(self, new_product):   #* Esta función agrega los productos al dict (comenzando con el indice 1 para que coincida con nuestra forma de contar) 
        self.products_dict[len(self.products_dict) + 1] = new_product  #Posteriormente en la clase Sales_manage en la función create_product se asocia el indice con la variable sale_number
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def get_product(self, number_by_user):   #*Esta función es para obtener un producto determinado (por numero de producto)
        return self.products_dict.get(number_by_user)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def update_products(self):    #* Función para actualizar datos despues de realizar una modificacion, tanto del dict como del txt
        updated_products_dict = {}    #Diccionario (temporal) para almacenar los productos actualizados en el orden correcto
        for index, product in enumerate(self.products_dict.values(), start=1): #*Loop for para obtener los elementos del diccionario ya modificado, obteniendo values(el producto) comenzando por el indice 1 
            updated_products_dict[index]=product                                                #*Para reasignar el # de producto correctamente desde el índice 1 en el (dict temporal) y estecoindida con el numero de venta actualizado
                                                                                                #*ya que los items en products_dict quedaron desfasados debido a la eliminacion de un producto
        self.products_dict = updated_products_dict   #Se llama al diccionario modificado para actualizarlo con la informacion del diccionario temporal

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def change_product_info(self):    #* Funcion para cambiar datos del prodcuto seleccionado (ya sea nombre, cantidad o precio)
        from sale_manager import SALE_Manager
        self.class_sale = SALE_Manager()   #*Instancia para llamar a la clase SALE_Manager() y sus funciones dentro de esta clase principal
        while True:   #Bucle para verificar que el numero de producto realmente exista
            self.class_sale.print_in_box("Please enter # of the product: ")
            try:
                number_by_user = int(input("------------------------->#: "))
                print("")

            except:
                print("")
                self.class_sale.print_in_box("-----> Please, enter a PRODUCT # <-----")
                print("")
            else:
                #Se llama a la funcion get_product() que es la que se encarga de buscar un producto por numero y lo retorna quedando disponible del producto para hacer modificaciones 
                current_product = self.get_product(number_by_user)
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
                            self.class_sale.print_in_box("Please, enter just a valid selection number")
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
                                        self.class_sale.print_in_box("Please, enter a valid quantity")
                                        print("")
                                    else:
                                        current_product.quantity = new_quantity
                                        break
                            elif change == 3 :
                                while True:
                                    try:
                                        self.class_sale.print_in_box(" Enter new price (Just number, no dollar sign)")                                             
                                        new_price = int(input("( ---> $: "))
                                        print("")
                                    except: 
                                        print("")
                                        self.class_sale.print_in_box("Please, enter a valid new price")
                                        print("")
                                    else:    
                                        current_product.price = new_price
                                        break
                        if change < 1 or change > 3:
                            self.class_sale.print_in_box("Please, enter a valid selection number")
                            print("")
                        
                        self.class_sale.update_info()
                        self.class_sale.consult()
                        self.class_sale.navigation()
                else:
                    self.class_sale.print_in_box("This product # doesn´t exist. ---> Please, try again...") #Si el numero de producto ingresado no existe se notifica al usuario y se repite el bucle
                    print("")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def remove_product (self):    #* Función para remover un producto (por #)
        from sale_manager import SALE_Manager
        self.class_sale = SALE_Manager()   #*Instancia para llamar a la clase SALE_Manager() y sus funciones dentro de esta clase principal
        while True:      #Igual que los anteriores loop de verificacion
            try:
                self.class_sale.print_in_box("Please enter # of the product to remove: ")
                print("")
                number_by_user=int(input("---> #: "))
                print("")
            except:
                print("")
                self.class_sale.print_in_box("-----> Please enter just a number <-----")
                print("")
            else:
                if number_by_user in self.products_dict:    #Si el numero de producto dado por el usuario existe:
                    del self.products_dict[number_by_user]  #El producto asosiaco a este se elimina del diccionario
                    self.class_sale.print_in_box("-----> Product deleted <-----")
                    self.update_info()     #Se actualiza los datos
                    self.consult()  #Y se devuelve en automatico para el usuario una consulta de los productos 
                    break   #Se rompe el loop una vez teminado el proceso
                else:
                    self.class_sale.print_in_box("-----> That sale # doesn´t exist... Please try again <-----")
                    print("")
        self.class_sale.navigation()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def sale_calculation(self):
        total_sum=0
        for index, product in self.products_dict.items() :
            product=self.get_product(index)
            total_sum+=(product.importt)
        self.class_sale.print_in_box(f"Total import: ${total_sum}")
        print("")
        self.class_sale.navigation()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------