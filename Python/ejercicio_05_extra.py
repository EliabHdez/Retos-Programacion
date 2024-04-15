""" 
    Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
        - Palíndromos
        - Anagramas
        - Isogramas
"""

def verification(word_1, word_2):
    # word_1 = word_1.replace(' ', '')
    # word_2 = word_2.replace(' ', '')
    # if word_1.lower() == word_2[::-1].lower() and sorted(word_1.lower()) == sorted(word_2.lower()):
    #     return print('Son Palíndromos y Anagramas')
    if word_1.lower() == word_2[::-1].lower():
        return print('Son Palíndromos')
    elif word_1.lower() == word_2.lower():
        print(f'No se considera Anagrama si la palabra o frase es la misma. ({word_1.upper()}, {word_2.upper()})')
    elif sorted(word_1.lower()) == sorted(word_2.lower()):
        print('Son Anagramas')
    else:
        print('No es ninguna de las 3')
        
verification('Luz azul', 'luza zul')
verification('Somos', 'som os')
verification('amor', 'ramo')
verification('amor', 'omar')
verification('ramo', 'ramo')
verification('amor', 'roma')
verification('amor', 'azul')
verification('Besos', 'sesos')
verification('amor', 'rosa')
verification('Alan Smithee', 'The Alias Men')

print('-----------------------------')

def is_isogram(word):
    word = word.lower()
    word = list(word)
    for element in word:
        count = word.count(element)
        if count == 2:
            word = ''.join(word)
            print(f'{word}: es un Isograma')
            break
    else:
        word = ''.join(word)
        print(f'{word}: NO es un Isograma')
        
is_isogram('Somos')
is_isogram('Negro')
is_isogram('Verde')
is_isogram('Moto')
is_isogram('Honda')

print('------------- Función del sorted ----------------')

name = 'Moises'
print(sorted(name.lower()))

one_list = ['Moises', 'Karla', 'Efrain', 'Hernandez', 'Cabello']
print(one_list)
print(sorted(one_list))

one_tuple = ('Moises', 'Karla', 'Efrain', 'Hernandez', 'Cabello')
print(one_tuple)
print(sorted(one_tuple))