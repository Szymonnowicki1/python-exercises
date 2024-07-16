# -*- coding: utf-8 -*-

# %%
techs = {'java', 'c++', 'python', 'sql'}
print(type(techs))
print(len(techs))

# %%
'python' in techs
 'elo' in techs

# %%
set('szymon')
set('ssssssymon')

# %%
techs.add('sas')

# %%
print(techs)

# %%
techs.remove('sas')

# %%
techs.pop()

# %%
techs.clear()

# %%
A = {1, 2, 3, 4, 5}
B = {1, 4, 6, 7, 8}
C = {6, 8}

C.issubset(B)
A.union(C)
A.intersection(B)
A.symmetric_difference(B)
D = A.copy()




























