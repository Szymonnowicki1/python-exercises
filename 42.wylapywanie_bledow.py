# -*- coding: utf-8 -*-
# %%
1 / 0

# %%
5 + '4'

# %%
int('g')

# %%
float('sd')

# %%
try:
    1 / 0
except:
    print('Nie dziel przez zero')
    
# %%
try:
    1 / 0
except ZeroDivisionError:
    print('Nie dziel przez zero')
except TypeError:
    print('Zły typ')

# %%
try:
    4 + '4'
except TypeError:
    print('Nie mozna dodac liczby i tekstu')
    
# %%
try:
    int('fd')
except ValueError:
    print('Zły tekst')
    
# %%
while True:
    try:
        x = int(input('Podaj liczbe :'))
        print(x)
        break
    except ValueError:
        print('Wprowadz liczbe')

# %%
def divide(x, y):
    try:
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError:
        print('Nie dziel przez zero')
    except ValueError:
        print('Wprowadz cyfre')
    
        
# %%
divide(3, 1)

# %%
divide(1, '5')

# %%
divide('1', 'f')



























