# -*- coding: utf-8 -*-

# %%
text = 'Witaj na kursie Pythona. \nPython jest wspaniały.'
print(text)

# %%
text.capitalize()

# %%
text.title() 

# %%
text.count('jest')

# %%
text.startswith('W')

# %%
text.endswith('ły.')

# %%
text.find('jest')
text[text.find('jest'):]

# %%
'Szymon123'.isalnum()

# %%
'475986'.isdigit()

# %%
'szymon'.islower()

# %%
'SZYMON'.isupper()

# %%
'#good#time#mood#game'.replace('#' , '  ')

# %%
'$'.join(['good' , 'game' , 'man'])

# %%
'       szympek      '.strip()
'       szympek      '.rstrip()
'       szympek      '.lstrip()

# %%
'176'.zfill(8)
'4'.zfill(6)

# %%
'#gym#fit#game#mood'.split('#')

# %%
print('#'.join(['sport' , 'python' , 'free' , 'time']))

# %%
x = '123,785,45,5'
x.split(',')
print(x.split(','))


























