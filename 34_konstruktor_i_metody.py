# -*- coding: utf-8 -*-

class Drzewo:
    
    def __init__(self, nazwa, wiek, wysokosc):
        self.nazwa = nazwa
        self.wiek = wiek
        self.wysokosc = wysokosc
        
    def czy_chronione(self):
        if self.wiek >= 20 and self.wysokosc >= 20:
            print('Drzewo o nazwie {} jest chronione'.format(self.nazwa))
        else:
            print('Drzewo o nazwie {} nie jest chronione'.format(self.nazwa))
    
        
    def postarz_o_rok(self):
        self.wiek += 1
            
drzewo_1 = Drzewo('sosna', 57, 36)
drzewo_2 = Drzewo('jodła', 4, 13)

# %%
print(drzewo_1.nazwa)
print(drzewo_2.wiek)

# %%
drzewo_1.czy_chronione()
drzewo_2.czy_chronione()

# %%
print(drzewo_2.wiek)
print(drzewo_2.postarz_o_rok())