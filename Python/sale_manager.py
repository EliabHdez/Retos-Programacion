##############################################################################################################################################################################################################################
class SALE_Manager:     #*Clase principal para gestionar el menu de sale_manager
    def __init__(self,hola = None):
        self.hola = hola
##############################################################################################################################################################################################################################
    def navigation(self): #* Nombre autodescriptivo xd 
        from product_manager import Product_NUMBER
        self.class_number = Product_NUMBER()   #*Instancia para llamar a la clase Sale_number() y sus funciones dentro de esta clase principal
        self.print_in_box("----> You´re in SALES management <-----")
        while True:
            try:
                print("---------------------------------------------------------------------------------------------------------------------")
                print("|                                              What do you need to do?                                              |")
                print("|                                                1: To add products                                                 |")           
                print("|                                             2: To remove any product                                              |")
                print("|                    3: To change any product information (Description, Quantity sold  or Price)                    |")
                print("---------------------------------------------------------------------------------------------------------------------\n")
                response=int(input("To continue, please type the number of your selection --> "))
                print("")
            except:
                print("")
                self.print_in_box("ERROR: Only numbers must be typed for a valid selection")
                print("#######################################################".center(117))
            else:
                if response < 1 or response > 3:
                    print("")
                    self.print_in_box("Please, enter a valid selection number")
                    print("######################################".center(117))
                else:
                    if response == 1:
                        self.class_number.create_product()
                    if response == 2:
                        self.class_number.remove_product()
                    if response == 3:
                        self.class_number.change_product_info()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def print_in_box(self,message, min_length = 113): #* Funcion para imprimir con formato en consola)
        length = max(len(message), min_length)     #-------------------------------------------------------------------------------------
        print("-" * (length + 4))                  #|             Formato de CAJA que centra el contenido automaticamente               |
        print("|", message.center(length), "|")    #-------------------------------------------------------------------------------------
        print("-" * (length + 4))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
start_SM= SALE_Manager()
start_SM.navigation()