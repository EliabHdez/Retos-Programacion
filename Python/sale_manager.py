##############################################################################################################################################################################################################################
class SALE_Manager:     #*Clase principal para gestionar el menu de sale_manager
    def __init__(self,hola = None):
        self.hola = hola
##############################################################################################################################################################################################################################
    def navigation(self): #* Nombre autodescriptivo xd 
        from product_manager import Product_NUMBER
        self.class_number = Product_NUMBER()   #*Instancia para llamar a la clase Sale_number() y sus funciones dentro de esta clase principal
        self.print_in_box("----> You´re in SALES management <-----")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("|                                              What do you need to do?                                              |")
        print("|                    1: To change any product information (Description, Quantity sold  or Price)                    |")
        print("|                                             2: To remove any product                                              |")
        print("|                                         3: To consult all sale´s products                                         |")
        print("|                                                4: To add products                                                 |")
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
                if response < 1 or response > 4:
                    print("")
                    self.print_in_box("-----> Please, enter a valid selection number <-----")
                    print("")
                else:
                    if response == 1:
                        self.class_number.change_product_info()
                    if response == 2:
                        self.class_number.remove_product()
                    if response == 3:
                        self.class_number.consult()
                    if response == 4:
                        self.class_number.create_product()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def print_in_box(self,message, min_length = 113): #* Funcion para imprimir con formato en consola)
        length = max(len(message), min_length)     #-------------------------------------------------------------------------------------
        print("-" * (length + 4))                  #|             Formato de CAJA que centra el contenido automaticamente               |
        print("|", message.center(length), "|")    #-------------------------------------------------------------------------------------
        print("-" * (length + 4))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
start_SM= SALE_Manager()
start_SM.navigation()