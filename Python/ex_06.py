# VARIABLES 'POR VALOR' Y 'POR REFERENCIA'

number = 5

def valor(num):
    number = 6
    num *= 2
    print(num)
    print(number)    

valor(number)

print(number)

languages = ['Python', 'C++', 'JavaScript']

def referencia(ref):
    for element in languages:
        if element == 'Python':
            languages[0] = 'Moto'
        if element == 'C++':
            languages[1] = 'Carro'
        if element == 'JavaScript':
            languages[2] = 'Avion'
    print(languages)
            
referencia(languages)

print(f'*** {languages} ***')

refer = ['Hola', 'Mundo']

def referencia(ref):
    refer[0] = 'Saludos'
    refer[1] = 'Terricolas'
    # refer = ['Bueeebos', 'Chotos']
    ref = refer
    print(ref)
    
referencia(refer)

print(f'*** {refer} ***')