# -*- coding: utf-8 -*-
# %%
i=3
j=i
i=2

# %%
a = 5

def fun_1():
    a = 3
    print(a)
    
fun_1()

# %%
tech = 'python'

def change_tech(new_tech):
    global tech
    tech = new_tech
   
change_tech('java')
print(tech)

# %%
level = 0

def f1():
    level = 1
    
    def f2():
        nonlocal level
        level = 2
        print('funkcja f2:', level)
        
    f2()
    print('funkcja f1:', level)

f1()
print('globalnie :', level)











































