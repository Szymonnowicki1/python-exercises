# -*- coding: utf-8 -*-
# %%
raw_data = '345!23!3234!43434!'
clean_data = ''
for x in raw_data:
    if  x != '!':
        clean_data += x
    else:
        clean_data += ','
print(clean_data)

# %%
suma = 0
for i in range(11):
    suma = suma + i
print(suma)

# %%
saldo = 450
print('Saldo początkowe {}' .format(saldo))
for kwota in range(10, 50, 10):
    print('wyplacona kwota {}' .format(kwota))
    saldo -= kwota
    print('Saldo {}' .format(saldo))
print('Saldo konconwe {}' .format(saldo))

# %%
print('Witaj w SFGAMES')
print('-' * 20)
nick = input('Podaj swoj nick:')
pin = input('Podaj swoj pin {} :' .format(nick))
if len(pin) == 4:
    for x in pin:
        if x in '0123456789':
            print('Poprawny PIN')
            break
        else:
            print('Zły PIN')
            break
else:
    print('Kod  PIN musi miec 4 cyfry ')
        





















































