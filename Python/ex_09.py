class motos:
    def __init__(self, brand, model, style, cc) -> None:
        self.brand = brand
        self.model = model
        self.style = style
        self.cc = cc
        
    def motos_specs(self):
        print('The Motorcycle is next:')
        # print(f'Moto {self.brand}:')
        print(' - Marca:', self.brand)
        print(' - Modelo:', self.model)
        print(' - Tipo:', self.style)
        print(' - Cilindrada:', self.cc)
        print('')
            
yamaha = motos('Yamaha', 'R7', 'Deportiva', '689')
yamaha.motos_specs()

honda = motos('Honda', 'CBR600RR', 'Deportiva', '600')
honda.motos_specs()

ducati = motos('Ducati', 'Pannigale', 'Deportiva', '899')
ducati.motos_specs()

kawasaki = motos('Kawasaki', 'H2R', 'Deportiva', '1200')
kawasaki.motos_specs()

ktm = motos('KTM', '450 EXC-F', 'Enduro', '450')
ktm.motos_specs()