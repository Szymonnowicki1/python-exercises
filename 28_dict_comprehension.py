# -*- coding: utf-8 -*-
# %%
stocks = {'amz' : 'amazon', 'appl' : 'apple', 'ggl' : 'google', 
          'ub' : 'uber'}

# %%
stocks.keys()
stocks.values()
stocks.items()

# %%
for key, value in stocks.items():
    print('{} : {}'.format(key, values))
    
# %%
stocks_dict = {key : value for (key, value) in stocks.items()}

# %%
stocks_invert = {value : key for (key, value) in stocks.items()}
print(stocks_invert)

# %%
stocks_upper = {key.upper() : value for (key, value) in stocks.items()}
print(stocks_upper)

# %%
stocks_set = {(key, value) for (key, value) in stocks.items()}

# %%
stocks_len = {key : value + ':' + str(len(value)) for (key, value ) in stocks.items()}

# %%
stocks_a = {key : value for (key, value) in stocks.items() if key.startswith('a') and len(key) < 4 }

# %%





































