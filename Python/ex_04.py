# Estructuras de datos

print('---------- Lists ----------')

# Lists

""" 
    Algunos metodos o acciones disponibles para listas son:
    
    - append
    - insert
    - remove
    - del (eliminar la variable que contiene la lista o bien eliminar un elemento en especifico de la lista)
    - pop
    - count
    - index
    - reverse
    - sort
    - clear
    - copy
"""

moto_honda = ['Honda', 'CBR600', 2003, 'F2']
print(type(moto_honda))
print(len(moto_honda))
print(moto_honda)
print(moto_honda[2:4])
print(moto_honda[0:-1])

print(moto_honda[3])
print(moto_honda[1])

moto_honda.append(1992)
print(moto_honda)

moto_honda.insert(2, 'Rojo')
print(moto_honda)

moto_honda.remove(2003)
print(moto_honda)

print(moto_honda.count('CBR600'))

del moto_honda[2]
print(moto_honda)

moto_honda_f2 = moto_honda.copy()
print(moto_honda_f2)

print(moto_honda.index('F2'))
print(moto_honda.index(1992))

moto_honda[3] = '1992' # Cambiamos el tipo de dato de int a str

moto_honda.sort() # El sort no puede acomodar los elementos de la lista si en esta hay diferentes tipos de datos
print(moto_honda)

moto_honda.clear()
print(moto_honda)
print(moto_honda_f2)

print('---------- Tuples ----------')

# Tuples

""" 
    Algunos metodos o acciones disponibles para tuplas son:
    
    - del (solo sirve para eliminar la variable que contiene la tupla)
    - count
    - index
    - in (Validamos si hay un elemento en especifico en la tupla)
"""

moto_honda = ('Honda', 'CBR600', 1992, 'F2', 1992, 2003)
print(type(moto_honda))
print(len(moto_honda))
print(moto_honda)
print(moto_honda[1])
print(moto_honda[3])

print(moto_honda.count('F2'))
print(moto_honda.count(1992))
print(moto_honda.count('honda'))

print(moto_honda.index(1992))
print(moto_honda.index('CBR600'))
print(moto_honda.index(2003))

print(moto_honda[1:3])
print(moto_honda[0:2])
print(moto_honda[2:6])
print(moto_honda[-1])

moto_honda_two = ('Honda', 'CBR600', 2003, 'RR')

motos_Honda = moto_honda + moto_honda_two

print(motos_Honda)

del moto_honda

# LAS TUPLAS SON INMUTABLES, POR LO TANTO NO PODEMOS MODIFICARLAS, ES DECIR, NO PODEMOS AGREGAR, ELIMINAR, NI REACOMODAR SUS ELEMENTOS. SI QUEREMOS HACER ALGUNA DE ESTAS ACCIONES TENDREMOS QUE CAMBIAR EL TIPO DE ESTRUCTURA DE DATO, ES DECIR PASAR UNA TUPLA A LISTA. PERO COMO TAL LAS TUPLAS NO PERMITEN NINGUNA DE ESTAS MODIFICACIONES

# Convirtiendo tupla a lista

print('---------- Convirtiendo tupla a lista ----------')

moto_honda = ('Honda', 'CBR600', 2003, 'RR')
print(type(moto_honda))
print(moto_honda)

moto_honda = list(moto_honda)
print(type(moto_honda))
print(moto_honda)

moto_honda.append('600cc')
print(moto_honda)

moto_honda.remove('CBR600')
print(moto_honda)

moto_honda.insert(1, 'CBR600RR')
print(moto_honda)

moto_honda[2] = '2003'
print(moto_honda)

moto_honda.reverse()
print(moto_honda)

moto_honda.sort()
print(moto_honda)

moto_honda = tuple(moto_honda)
print(type(moto_honda))
print(moto_honda)

print('Honda' in moto_honda)
print(2003 in moto_honda)
print('2003' in moto_honda)
print('RR' in moto_honda)

del moto_honda

print('---------- Sets ----------')

""" 
    Algunos metodos o acciones disponibles para tuplas son:
    
    - add
    - remove
    - pop (Elimina un elemento al azar del set)
    - clear
    - union (Crea un nuevo set juntando dos sets. Por lo tanto hay que crear una variable para la union)
    - difference
    - update (Inserta un set dentro de otro set determinado)
    - instersection (Devuelve un conjunto de elementos que se encuentran en ambos sets)
    - issubset (subset de un superset. No me queda claro que lo hace un subset)
    - issuperset (superset de otros sets. No me queda claro que lo hace un superset)
    - in (Validamos si hay un elemento en especifico en la tupla)
    - symmetric_difference (Devuelve los elementos que hay entre dos sets. Los elementos que devuelve son simetricos, es decir, devuelve los elementos tanto del primer set que no tiene el segundo y viceversa)
    - isdisjoint (Comprobamos si dos sets tienen uno o mas elementos en comun. Que sean completamente distintos o no. True si no hay elementos en comun y son distintos en su totalidad y False si hay elementos en comun, con un elemento que comportan ambos sets ya se considera que son completamente distintos)
    - del (solo sirve para eliminar la variable que contiene la tupla)
"""

moto_honda = {'Honda', 'CBR600', 2003, 'RR', 'Racing'}
print(type(moto_honda))
print(len(moto_honda))
print(moto_honda)

moto_honda.add('600cc')
print(moto_honda)

moto_honda.remove('CBR600')
print(moto_honda)

moto_honda.add('CBR600RR')
print(moto_honda)

moto_honda_f2 = {'Honda', 'CBR600', 1992, 'F2', 'Racing'}

motos_Honda = moto_honda.union(moto_honda_f2)
print(motos_Honda)

print(moto_honda.difference(moto_honda_f2))

print('Racing' in motos_Honda)
print('Racing' in moto_honda)
print('Deportiva' in motos_Honda)
print(2003 in moto_honda)
print(1992 in moto_honda_f2)
print('Rojo' in motos_Honda)
print('Blanco' in motos_Honda)

print(moto_honda_f2)
delete_element = moto_honda_f2.pop()
print(moto_honda_f2)
print(delete_element)

print(moto_honda.intersection(moto_honda_f2))

# moto_honda.update(moto_honda_f2)
moto_honda_f2.update(moto_honda)
print(moto_honda)

print(moto_honda)
print(moto_honda_f2)

print(moto_honda.issubset(moto_honda_f2))
print(moto_honda.issuperset(moto_honda_f2))
print(moto_honda_f2.issuperset(moto_honda))
print(moto_honda_f2.issubset(moto_honda))

moto_honda = {'Honda', 'CBR600', 2003, 'RR', 'Racing'}

moto_honda_f2 = {'Honda', 'CBR600', 1992, 'F2', 'Racing'}

print(moto_honda.symmetric_difference(moto_honda_f2))

moto_yamaha = {'Yamaha', 'YZF6', 2010, 'R6', 'Carreras'}

print(moto_honda.isdisjoint(moto_yamaha))
print(moto_honda.isdisjoint(moto_honda_f2))

motos_Honda.clear()
print(motos_Honda)

del motos_Honda

print('---------- Dictionaries ----------')

""" 
    Algunos metodos o acciones disponibles para diccionarios son:
    
    - items
    - keys
    - values
    - fromkeys
    - del -> Elimina la variable que contiene el diccionario o un elemento del diccionarios si se lo especificamos
    - pop -> Elimina el elemento que le pasemos por clave
    - popitem -> Elimina el ultimo elemento
    - copy
    - clear
    - get -> Nos permite verificar si existe una clave en el diccionario. Si existe nos devuelve el valor de la clave, si NO existe no devuelve 'None'
"""

moto_yamaha = {
    'Marca':'Yamaha',
    'Modelo':'YZF6',
    'Año':2010,
    'Versión':'R6',
    'Specs':{
        'Motor':'600cc',
        'Suspensión':'Invertida',
        'Frenos':'Doble disco ventilado'
    }
    }
print(type(moto_yamaha))
print(len(moto_yamaha))
print(moto_yamaha)

print(moto_yamaha['Marca'])
print(moto_yamaha['Modelo'])
print(moto_yamaha['Versión'])
print(moto_yamaha['Specs'])
print(moto_yamaha['Specs']['Motor'])
print(moto_yamaha['Specs']['Suspensión'])

moto_yamaha['Tipo'] = 'Deportiva'
print(moto_yamaha)

moto_yamaha['Tipo'] = 'Racing'
print(moto_yamaha['Tipo'])

moto_yamaha['IP'] = 'Yamaha Industries'
print(moto_yamaha)

moto_yamaha['Country'] = 'Japan'
print(moto_yamaha)

moto_yamaha['Specs']['Motor'] = 600
print(moto_yamaha['Specs'])

moto_yamaha['Specs']['Potencia'] = '192 HP'
print(moto_yamaha['Specs'])

del moto_yamaha['IP']
print(moto_yamaha)

moto_yamaha['IP'] = 'Yamaha Industries'
print(moto_yamaha['IP'])
print(moto_yamaha)

moto_yamaha.pop('IP')
print(moto_yamaha)

print('Marca' in moto_yamaha)
print('Brand' in moto_yamaha)
print('Modelo' in moto_yamaha)
print('Model' in moto_yamaha)
print('Specs' in moto_yamaha)
print('Motor' in moto_yamaha) # El 'in' no valida claves de diccionarios que estan dentro de otro dict
# Las claves de un dict dentro de otro dict Python las toma como valores, no como claves
print('Engine' in moto_yamaha)

print(moto_yamaha.items()) # Crea una lista con tuplas donde cada tupla es una clave:valor
print(moto_yamaha.keys()) # Nos da todas las claves de un diccionario como una lista
print(moto_yamaha.values()) # Nos da todos los valores de las claves del diccionario como una lista. Claves del dict dentro de otro dict como valores

new_moto = moto_yamaha.copy()

new_yamaha = dict.fromkeys({
    'Marca',
    'Modelo',
    'Versión',
    'Año',
    'Variantes'
})
print(new_yamaha)

new_yamaha['Modelo'] = 'YZF1'
new_yamaha['Versión'] = 'R1'
print(new_yamaha)
print(new_yamaha.get('Specs'))
print(new_yamaha.get('Versión'))

new_yamaha = dict.fromkeys(moto_yamaha)
print(new_yamaha)

new_yamaha = dict.fromkeys(moto_yamaha, ('Sin información'))
print(new_yamaha)

print(new_moto)
new_moto.clear()
print(new_moto)

new_yamaha = {
    'Marca':'Yamaha',
    'Modelo':'YZF',
    'Versión':'R Type',
    'Año':'1998+',
    'Variantes':[]
}

new_yamaha['Type'] = 'Racing'
new_yamaha['Variantes'].append('R1')
new_yamaha['Variantes'].append('R6')
print(new_yamaha)

new_yamaha.pop('Año')
print(new_yamaha)

new_yamaha.popitem()
print(new_yamaha)

def ParImpar():
    while True:
        try:
            numero = int(input('Introduce un numero '))
            print('Su numero es ', numero, ', ', end=(''))
            if numero % 2 == 0:
                print('por ende es Par.')
            else:
                print('por ende es Impar.')
            break
        except ValueError:
            print("Debe ingresar un valor enteror")
    return numero