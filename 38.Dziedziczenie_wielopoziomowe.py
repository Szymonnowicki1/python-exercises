# -*- coding: utf-8 -*-
# %%

class Czlowiek:
    
    pochodzenie = 'Ziemia'
    imie = 'Andie'
    
class Polak(Czlowiek):
    
    kraj = 'Polska'
    # imie = 'Szymon'
    
class Programista(Polak):
    
    technologia = 'python'
    # imie = 'Krzysztof'
    
    def info(self):
        print('Obiekt pochodzenia to : {}'.format(self.pochodzenie))
        print('Kraj pochodzenia to : {}'.format(self.kraj))
        print('Technologia to : {}'.format(self.technologia))
        print('Imie to : {}'.format(self.imie))
              
# %%
programista_1 = Programista()

# %%
programista_1.info()     

