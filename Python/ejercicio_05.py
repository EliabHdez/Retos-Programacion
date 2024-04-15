# Cadena de caracteres

saludo = 'Hola Mundo'

print('------- Acceso a caracteres específicos ---------')

print(saludo[0])
print(saludo[1])
print(saludo[3])
print(saludo[5])
print(saludo[6])
print(saludo[9])
print(saludo[-1])
print(saludo[-5])
print(saludo[::-1])

print('------- Subcadenas o slicing ---------')

print(saludo[2:6])
print(saludo[:8])
print(saludo[0:4])
print(saludo[3:])
print(saludo[3:-2])
print(saludo[-2:-3])
print(saludo[-4:-1])
print(saludo[:-6])
print(saludo[-9:])

print('------- Longitud ---------')

palabra_1 = 'Moto'
palabra_2 = 'Honda CBR600RR'

print(len(saludo)) # Cuenta los espacios
print(len(palabra_1))
print(len(palabra_2))

print('------- Concatenación ---------')

lenguaje = 'Py' 'thon'
cool = 'rifa'
cool_2 = ' rifa'
concat = palabra_1 + ' ' +  palabra_2

print(lenguaje)
print(lenguaje + ' ' + cool)
print(lenguaje + cool_2)
print(concat)
print(concat + ' de las mejores')
print(concat + cool_2 + ', de las mejores')
print(f'{palabra_1} {palabra_2}, es de las mejores... {cool.capitalize()}!!!')

print('------- Repetición ---------') # Tenia duda con respecto a la repetición, pero hacia referencia a poder repetir la cadena de texto

print(palabra_1 * 3)
print(palabra_2 * 2)
print(cool * 5)

print(palabra_1.count('M'))
print(palabra_1.count('o'))
print(palabra_1.count('cicleta'))
print(palabra_2.count('Honda'))
print(palabra_2.count('RR'))
print(palabra_2.count('R'))
print(palabra_2.count('nd'))
print(palabra_2.count('6'))
print(palabra_2.count('0'))
print(palabra_2.count('600'))
print(saludo.count('Hola'))
print(saludo.count('Mundo'))
print(saludo.count('M'))
print(saludo.count('H'))
print(saludo.count('la'))
print(saludo.count('do'))

print('------- Recorrido ---------')

for element in saludo:
    print(element)
print('*****')
    
for element in palabra_1:
    print(element)
print('*****')
    
for element in palabra_2:
    print(element)
print('*****')
    
for element in lenguaje:
    print(element)
print('*****')
    
for element in cool:
    print(element)
print('*****')
    
for element in cool_2:
    print(element)
print('*****')
    
for element in concat:
    print(element)
print('*****')

print('------- Conversion a mayúsculas y minúsculas ---------')

print(palabra_2)
palabra_2 = 'honda Cbr600RR'
print(palabra_2)
print(palabra_2.capitalize())
print(palabra_2.upper())
print(palabra_2.isupper()) # Marca false porque en la cadena de texto hay numeros
print(palabra_1.upper().isupper())
print(palabra_2.lower())
print(palabra_2.islower()) # Marca false porque en la cadena de texto hay numeros
print(palabra_2.isnumeric())
print(palabra_2.isalnum())
print(palabra_2.isalpha())
print(palabra_2.isalpha())

print('-----')

palabra_numeros = '1990'
print(palabra_numeros.isnumeric())
print(palabra_numeros.isalnum())
print(palabra_numeros.isalpha())
print(palabra_numeros.isdigit())

print('------- Reemplazo ---------')

saludo = 'Hola Python'
print(saludo.replace('Python', 'Javascript'))

conversando = 'Hola Karlita, como estas corazón???'
print(conversando)
reemplazo_1 = conversando.replace('Karlita', 'amor')
print(reemplazo_1)
reemplazo_2 = reemplazo_1.replace('corazón', 'bombón')
print(reemplazo_2)

print('------- Interpolación o Formateo ---------')

name = 'Karlita'
hunny = 'corazón'

print('--- Marcadores de posición ---')

saludo_2 = 'Hola {}, como estas {}???'
print(saludo_2.format(name, hunny))
print('-----')
print(saludo_2.format('amor', 'bombom'))

print(saludo_2.format('putin', 'perro'))

print('--- Marcadores de posición numerado ---')

saludo_2 = 'Hola {1}, como estas {0}???'
print(saludo_2.format('bro', 'mi estimado'))

print('--- Marcadores de posición con nombres ---')

saludo_2 = 'Hola {name}, como estas {alias}???'
print(saludo_2.format(name='Janeth', alias='niña'))

print('--- F-String ---')

name_1 = 'Clau'
alias_1 = 'amiga'

print(f'Que ovo {alias_1}, como estas {name_1}???')

print('------- Union/Join ---------')

# La función join() nos puede servir para pasar una lista a cadena de texto

print(palabra_2.join(palabra_1))

list_one = ['H', 'e', 'l', 'l', 'o']
text_from_list = ''.join(list_one)
print(text_from_list)

# Mas ejemplos en la parte final del archivo

print('------- Verificación ---------')

print('H' in saludo)
print('h' in saludo)
print('o' in saludo)
print('l' in saludo)
print('M' in saludo)
print('m' in saludo)
print('u' in saludo)
print('d' in saludo)

print('----------------')

print('Hola' in saludo)
print('hola' in saludo)
print('Hol' in saludo)
print('Mundo' in saludo)
print('Mun' in saludo)
print('mundo' in saludo)
print('mun' in saludo)
print('do' in saludo)

print('----------------')

print('------- Division ---------')

print(saludo.split())
print(saludo.split('t'))
print(saludo_2.split())
print(palabra_2.split())
print(palabra_2.split('600'))
print(palabra_2.split('RR'))

print('------- De lista a cadena ---------')

one_list = ['M', 'o', 't', 'o']
text = ''.join(one_list)
print(text)
print(type(text))

palabra_2 = 'Honda CBR600RR'

print(palabra_2.find('CBR600RR'))