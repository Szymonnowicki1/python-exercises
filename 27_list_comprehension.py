# -*- coding: utf-8 -*-
# %%
lista = []

for i in range(100):
    lista.append(i ** 2)
    
print(lista)

# %%
lista_2 = [i ** 2 for i in range(100)]

# %%
lista_3 = [i  * 3for i in range(100)]

# %%
lista_4 = [i ** 2 for i in range(100) if i % 5 == 0]

# %%
letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']
pusta_lista = []
for letter in letters:
    for number in numbers:
        pusta_lista.append(letter + number)

# %%
pusta_lista_1 = [letter + number for letter in letters for number in numbers]

# %%
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

results = [pierwszy + drugi for pierwszy in x for drugi in y if pierwszy != drugi]

# %%
[[j for j in range(10)]for i in range(10)]

# %%
[[(i, j)for j in range(10)]for i in range(10)]

# %%
[[j * i for j in range(10)]for i in range(10)]

# %%
[[l_2 + l_1 for l_2 in '1234'] for l_1 in 'abcd' ]

# %%
[ i for i in range(30) if i % 4 == 0 ]






































