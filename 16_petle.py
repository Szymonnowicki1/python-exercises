# -*- coding: utf-8 -*-
# %%
name = 'python'
for x in name:
    print(x)
    
# %%
name = 'sql'
index = 0
for y in name:
    print(index, y)    
    index = index + 1
    
# %%
for x in range(21):
    print(x)
    
# %%
hashtags = '#weekend#good#time#' 
result = ''   
for x in hashtags:
    if x not in '#':
        result = result + x
    else:
        if result:
            print(result)
            result = ''

# %%
slowo = 'Python Course'
for x in slowo:
    if x == 'u':
        break
    print(x)
    
# %%
for x in 'ardwin123@wp.pl':
    if x == '@':
        print('Mamy to')
        break
else:
    print('Nie pasuje')
    
# %%
ps = 'jnhvsoics!vd'  
if len(ps) > 10:
    for x in ps:
        if '!' in ps:
            print('Hasło poprawne')
            break
    else:
            print('Hasło niepoprawne')
else:
    print('Hasło niepoprawne')

# %%
sample = 'Python Course'
for x in sample:
    if x == ' ':
        continue
    print(x)
    
# %%
for y in range(8):
    if y ==5:
        continue
    print(y)
    
# %%
lista = [1, 2, 99, 4, 5]
for x in lista:
    if x == 99:
        continue
    print(x)
    
        
        


















































