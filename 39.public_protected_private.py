# -*- coding: utf-8 -*-
#  public = zmienna
#  protected = _zmienna
# private = __zmienna

# %%
class Spolka:
    
    def __init__(self, rodzaj, rynek, gielda):
        self.rodzaj = rodzaj
        self.rynek = rynek
        self.gielda = gielda
        
class KGHM(Spolka):
        
        def __init__(self, rodzaj, rynek, gielda, nazwa):
            super().__init__(rodzaj, rynek, gielda)
            self.nazwa = nazwa
            print('atrybut publiczny : {}'.format(self.rodzaj))
            print('atrybut chroniony : {}'.format(self.rynek))
            print('atrybut prywatny : {}'.format(self.gielda))
            
# %%
spolka = Spolka('spolka akcyjna', 'główny', 'GPW w warszawie')

print('atrybut publiczny : {}'.format(spolka.rodzaj))
print('atrybut chroniony : {}'.format(spolka.rynek))
print('atrybut prywatny : {}'.format(spolka.gielda))
# %%
      
kghm = KGHM('spolka akcyjna', 'glowny', 'GWP w warszawie', 'KGHM')
print('atrybut prywatny : {}'.format(self.gielda))