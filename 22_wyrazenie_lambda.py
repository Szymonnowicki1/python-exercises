# -*- coding: utf-8 -*-
# %%
def parabola(x):
    return x ** 2 + 3

print(parabola(30))

# %%
add = parabola
print(add(30))

# %%
parabola = lambda x: x ** 2 + 3
parabola(30)

# %%
f = lambda x, y: x + y
f(4, 7)

# %%
t = lambda text: text.upper()
t('python')

# %%
lista = ['python', 'sql', 'c++']
list(map(lambda word: word.upper(), lista))

# %%
list(map(lambda word: (word, len(word)), lista))

# %%
def funkcja_1(x, funkcja):
    return funkcja(x)

funkcja_1(10, lambda x: x ** 2)


# %%
numbers = [ 5, 6, 3, 8, 12, 7]
sorted(numbers)

number = [-2, -1, 0, 1, 2]
sorted(number, key= lambda x: abs(x))

# %%
city = ['Warsaw', 'London', 'Berlin', 'New York'] 
list(map(lambda word: word[:3], city))



# %%
x = 'python'
x[:3]















































