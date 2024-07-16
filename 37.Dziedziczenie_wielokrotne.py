# -*- coding: utf-8 -*-
# %%

class Czlowiek:
    
    pochodzenie = 'Ziemia'
    imie = 'Andie'
    
class Polak:
    
    kraj = 'Polska'
    imie = 'Szymon'
    
class Pilkarz(Polak, Czlowiek):
    
    def info(self):
        print('Utworzony obiekt pochodzi z planety {}.\nKraj pochodzeni to {}.\nNazwa obiektu: {}'
              .format(self.pochodzenie, self.kraj, self.imie))
        
# %%
pilkarz_1 = Pilkarz()
pilkarz_1.info()






















