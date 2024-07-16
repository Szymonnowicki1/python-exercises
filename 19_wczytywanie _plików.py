# -*- coding: utf-8 -*-

# %%
with open('plik', 'r') as file:
    for line in file:
        print(line, end='')
        
# %%
with open('plik', 'r') as file:
    x = file.readlines()

print(x, end='')

# %%
lista = ['java', 'c++', 'sql', 'python']
with  open('plik z zajec', 'w') as file:
    for x in lista:
        print(x, file=file)
      
# %%
even_numbers = list(range(100))[::2]
with open('numbers', 'w') as file:
    for numbers in even_numbers:
        file.write(str(numbers) + '\n')
        
# %%
technologies = []
with open('plik', 'r') as file:
    for line in file:
        technologies.append(line[:-1])
print(technologies)

# %%       
with open('choinka', 'w') as file:
    for j in range(2):
        for i in range(10):
            print('{:>9}'.format('*' * i), end='', file=file)
            print('{}'.format('*' * i), file=file)



























