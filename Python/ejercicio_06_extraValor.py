# FUNCIONES PASO DE VARIABLE POR VALOR

text = 'Katana es una gorda bella'
number = 1990

# INTERCAMBIANDO LOS VALORES DE LAS VARIABLES ENTRE ELLAS

def valores(text, number):
    change = text
    text = number
    number = change
    return text, number

values = valores(text, number)

# ALMACENANDO RETORNO DE VALORES EN VARIABLES DIFERENTES A LAS ORIGINALES

print('----- Variables dif to or -----')

text_value = values[0]
num_value = values[1]
print(text_value)
print(num_value)

# IMPRESION VARIABLES ORIGINALES

print('----- Original variables -----')

print(f'* {text} *')
print(f'* {number} *')

print('----- Global Variable -----')

# UTILIZANDO GLOBAL DENTRO DE LA FUNCION PARA REFERIRNOS A UNA VARIABLE EXTERNA A ESTA. DE ESTA MANERA VEREMOS QUE LA COSA CAMBIA CON RESPECTO A ESTA VARIABLE. PORQUE? PORQUE AL HACER USO DE GLOBAL, LO HACEMOS PARA TRABAJAR CON LA VARIABLE EXTERNA EN CUESTION COMO TAL, POR LO TANTO COMO YA NOS ESTAMOS REFIRIENDO A ESA VARIABLE DE FORMA DIRECTA AHORA SI QUE SI LOS CAMBIOS QUE LE HAGAMOS A ESA VARIABLE AUN DENTRO DE LA FUNCION TAMBIEN SE VAN A VER REFLEJADOS FUERA DE LA FUNCION

def valores_1(val_1, val_2):
    val_op = val_1
    val_1 = val_2
    val_2 = val_op
    global text
    print(text)
    print(number)
    text = 'Hey you'
    print(text)
    return text, number, text

values_1 = valores_1(text, number)
print(values_1)

# IMPRESION VARIABLES ORIGINALES DESPUES DE USAR GLOBAL

print('----- Original variables con global -----')

print(f'* {text} *')
print(f'* {number} *')