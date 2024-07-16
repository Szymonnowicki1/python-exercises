# -*- coding: utf-8 -*-
# %%

class Czlowiek:
    
    def __init__(self, imie, nazwisko):
        sel.imie = imie
        self.nazwisko = nazwisko
        
    def info(self):
        print('{} {}'.format(self.imie, self.nazwisko))
        
    
class Pilkarz(Czlowiek):
    
    def __init__(self, imie, nazwisko, klub):
        self.imie = imie
        self. nazwisko = nazwisko
        self.klub = klub
        
    def info(self):
        super().info()
        print('Klub : {}'.format(self.klub))
        
# %%
pilkarz_1 = Pilkarz('leo', 'messi', 'FC barcelona')
pilkarz_2 = Pilkarz('robert', 'lewandowski', 'bayern')

# %%
pilkarz_1.info()
pilkarz_2.info()

# %%




































