# -*- coding: utf-8 -*-
# %%

class Drzewo:
    
    nazwa = 'Sosna'
    wiek = 40
    wysokosc = 25
    
drzewo_1 = Drzewo()
drzewo_2 = Drzewo()

# %%
print(id(drzewo_1))
print(id(drzewo_2))

# %%
dir(drzewo_1)

# %%
drzewo_1.nazwa
drzewo_1.wiek

# %%
drzewo_2.nazwa

# %%
drzewo_1.stan = 'dobry'

print(dir(drzewo_1))

# %%
Drzewo.miejsce = 'las'