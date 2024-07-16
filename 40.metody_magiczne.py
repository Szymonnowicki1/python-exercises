# -*- coding: utf-8 -*-
1 + 1

# %%
type(1)

# %%
dir(int)

# %%
int.__add__(2, 7)

# %%
int.__sub__(4, 7)

# %%

class SpecialInt(int):
    
    def __init__(self, special_int):
        self.special_int = special_int
        
    def __add__(self, other):
        return self.special_int + other.special_int + 10
    
    def __sub__(self, other):
        return self.special_int - other.special_int -10
    
    def __lt__(self, other):
        return self.special_int < other.special_int 

# %%
s_1 = SpecialInt(2)
s_2 = SpecialInt(3)

# %%
s_1 + s_2

# %%
s_1 - s_2

# %%
s_1 < s_2 



















