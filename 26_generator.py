# -*- coding: utf-8 -*-
# %%
def generator():
    yield 4
    yield 5
    yield 6
    
# %%
gen = generator()

# %%
next(gen)

# %%
def generator_2(word):
    letters = list(word)
    for letter in letters:
            yield letter

# %%            
gen_2 = generator_2('siema')
 
 # %%
next(gen_2)

# %%
file = ['java.py', 'python.py', 'sql.txt']

def generator_3(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item
            
gen = generator_3(file)

# %%
next(gen)

# %%
for i in gen:
    print(i)
    
# %%
files = ['run_me.py', 'README.md', 'help.txt.', 'script.py', 'menu.py', 'main.py', 'py']

def generator_py(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item































