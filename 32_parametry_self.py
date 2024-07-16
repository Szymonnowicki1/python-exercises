# -*- coding: utf-8 -*-

# %%
class Drzewo:
    
    def wyswietl_info_o_drzewie(self):
        self.nazwa = 'Sosna'
        self.wiek = 40
        self.miejsce = 'las'
        print(f'Drzewo nazywa sie {self.nazwa}, ma {self.wiek} lat i znajduje sie w {self.miejsce}')

drzewo = Drzewo()

# %%
drzewo.wyswietl_info_o_drzewie()