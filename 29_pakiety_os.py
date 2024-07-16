# -*- coding: utf-8 -*-

# %%
import os

# %%
dir(os)

# %%
os.getcwd()

# %%
os.chdir('C:\\Users\\szymu\\OneDrive\\Pulpit\\kurs\\python_kurs')

# %%
os.getcwd()

# %%
os.system('mkdir dir1 dir2 dir3')

# %%
os.rmdir('dir2')

# %%
os.listdir()

# %%
for item in os.listdir():
    if item.endswith('.py'):
        print(item)
        
# %%
for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)
