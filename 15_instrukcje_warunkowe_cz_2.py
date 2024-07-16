# -*- coding: utf-8 -*-

# %%
print('Witaj w bankomacie')
print('Włam się do systemu, zgadując dwucyfrowy numer pin.\nNumer pin składa sie z liczb 0, 1, 2.')
pin = int(input('Siema. Podaj numer pin:'))
if pin == 20:
    print('Poprawny pin')
elif pin == 10:
    print('Prawie masz to')
else:
    print('Zły pin')
    
# %%
number = 3
if number :
    print('licza niezerowa')
else:
    print('zero')
    
# %%
flag = False
if flag:
    print('doszło')
else:
    print('nie doszło')
    
# %%
v = '55km/h'
if v > '50km/h':
    print('Zwolnij!')
else:
    print('Tak trzymaj!')

# %%
saldo = 1000
klient_zweryfikowany = True
if saldo > 0 and klient_zweryfikowany:
    print('Mozesz wypłącic kase')
else:
    print('Nie mozesz wyplacic kasy')

# %%
saldo = 1000
klient_zweryfikowany = True
kwota = int(input('Ile chcesz wypłacic:'))
if saldo > 0 and klient_zweryfikowany and saldo >= kwota:
    print('Mozesz wypłącic kase')
else:
    print('Nie mozesz wyplacic kasy.\nBrak wystarczajacej kasy{}'.format(abs(saldo - kwota)))
    
# %%
fakt = 'python jest łatwy i przyjemny'
a = (list(fakt))
print(a)
if a > 20:
    print('Mniej niż 20 unikalnych znaków')
else:
    print('Liczba unikalnych znaków jest większa lub równa 20.')

# %%
fakt = 'python jest łatwy i przyjemny'
characters = list(fakt)
print(characters)
x = len(set(characters))
if x < 20:
    print('Mniej niż 20 unikalnych znaków.')
else:
    print('Liczba unikalnych znaków jest większa lub równa 20.')
    
    # %%
len(set(characters))

# %%
'a' in 'python'

# %%
tech = 'python'
'ok' if tech == 'python' else 'not'

# %%
text = 'sfdvjklncdnskjccbnksjdnckjsdsnckjnsdkjnckjsnkjlcnqdlknwsx'
print('Zawiera' if 'q' in text else 'Nie zawiera')






















































