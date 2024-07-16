# -*- coding: utf-8 -*

# %%
def funkcja_1 ():
    print('Uruchumiono 1 funkcje')

funkcja_1()

# %%
def funkcja_2(x = 4, y = 6):
    print('Podano 2 argumenty x={} i y={}'.format(x,y))
    
funkcja_2()

# %%
import math
math.sqrt(9)
math.sin(1)

# %%
def add(x, y):
    return x + y

add(4, 7)

# %%
def funkcja_menu():
    print('Witaj w programie')
    print('-' * 30)
    print(""" Wybierz jenda z opcji
          1 = logowanie
          2 = wyjscie z programu""")
    print('Koniec programu')

funkcja_menu()

# %%
def policz_srednia(x, y, z):
    return (x + y + z) / 3 

# %%
def print_even(maximum):
    lista = []
    for i in range(maximum + 1):
        if i % 2 == 0:
            lista.append(i)
    return lista
    
print_even(10)
x = print_even(20)

# %%
def write_file(file_name, text):
    with open(file_name, 'w') as file:
        print(text, file=file)
        
write_file('zadanie', 'Siema\nCo\nTam')

# %%
def drukuj_nieparzyste(liczby_nieparzyste = 20):
    lista = []
    for i in range(liczby_nieparzyste):
        if i % 2 != 0:
            lista.append(i)
    return lista

# %%
def add(x, y):
    """ Ta funkcja dodaje 2 argumenty
    Inputs:
        a = int
        b = int
    Outputs:
        suma = int"""
    return x + y
            
help(add)








































































