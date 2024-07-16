# -*- coding: utf-8 -*-
import numpy as np


class FunkcjaKwadratowa:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def make_function(self):
        print(f'{self.a} * x ** 2 + {self.b} * x + {self.c}')
        
    def rozwiaz(self):
        if self.a == 0 and self.b == 0 and self.c == 0 :
            print('Rownanie tożsamosciowe')
        elif self.a == 0 and self.b == 0 and self.c != 0:
            print('Rownanie sprzeczne')
        elif self.a == 0 and self.b != 0 :
            x = self.c / self.b
            print(x)
        elif self.a != 0:
            delta = self.b ** 2 - 4 * self.a * self.c
            if delta > 0:
                sqrt_delta = np.sqrt(delta)
                x1 = (-self.b - sqrt_delta) / ( 2 * self.a)
                x2 = (-self.b + sqrt_delta) / ( 2 * self.a)
                print(x1, x2)
            elif delta == 0:
                x = - self.b / 2 * self.a
                print(x)
            elif delta < 0:
                print('Brak rozwiazan')
                
# %%
fk = FunkcjaKwadratowa(3, 1, -4)
fk.make_function()

# %%
fk.rozwiaz()

# %%
numbers = [23, 12, 53, 13, 65, 1, 45]
x = 13
while x in numbers:
    if x ==13:
        print('Znaleziono')
        break
    
# %%
text = 'python jest popularny w uczeniu maszynowym'
print(len({x for x in list(text)}))













