# -*- coding: utf-8 -*-

# %%
d = {}
type(d)

# %%
pol_to_eng = {'jeden' : 'one', 'dwa' : 'two', 'trzy' : 'three'}

# %%
name_to_digit = {'jeden' : 1, 'dwa' : 2}

# %%
name_to_liczby = {0 : 1, 1:2, 2:3}

# %%
pol_to_eng['cztery'] = 'four'

# %%
pol_to_eng.clear()

# %%
pol_to_eng12 = pol_to_eng.copy()


# %%
pol_to_eng.keys()

# %%
pol_to_eng.values()

# %%
pol_to_eng.items()

# %%
pol_to_eng['dwa']

# %%
pol_to_eng.pop('dwa')

# %%
pol_to_eng.popitem()

# %%
pol_to_eng.update({'jeden' : 1})

# %%
slownik = {1:1, 2:4, 3:9, 4:16, 5:25}
print(slownik)

# %%
capitals = {'Polska': 'Warszawa', 'Niemcy': 'Berlin', 'Czechy': 'Praga'}
capitals.update({'Włochy' : 'Rzym'})
stolice = sorted(list(capitals.values()))
print(stolice)












































