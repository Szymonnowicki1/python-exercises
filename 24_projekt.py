# -*- coding: utf-8 -*-
# %%
import datetime
import time

print(datetime.datetime.utcnow())

# %%
def log(message, dt = datetime.datetime.utcnow()):
    print(dt, message)
    
log('uruchomiono')

# %%
def logi(*args):
    for i in args:
        log(i)
        time.sleep(1)
        
logi('uruchomiono', 'system', 'czekaj')
        































