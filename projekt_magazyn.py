# -*- coding: utf-8 -*-

# %%

import sys
 
class Magazyn:
    
    def __init__(self, lista_produktow):
        self.lista_produktow = lista_produktow
        
    def wyswietl_dostepne_produkty(self):
        print('Dostepne produkty')
        for produkt in self.lista_produktow:
            print(produkt)
            
    def dodaj_produkt(self):
        self.nazwa_produktu = input('Podaj nazwe produktu :')
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)
            print('Produkt {} został dodany do listy'.format(self.nazwa_produktu))
            
    def usun_produkt(self):
        self.nazwa_produktu = input('Podaj nazwe produktu ktory chcesz usunac :')
        if self.nazwa_produktu in self.lista_produktow:
            self.lista_produktow.remove(self.nazwa_produktu)
            print('Usunieto produkt')
        else:
            print('Nie ma takiego produktu w magazynie')
            
# %%
magazyn = Magazyn(['woda', 'czekolada', 'kalafior', 'cola'])

while True:
    print('Wybierz 1 aby zobaczyc produkty w magazynie')
    print('Wybierz 2 aby dodac produkt do magazynu')
    print('Wybierz 3 aby usunac produkt z magazynu')
    print("wybierz 4 aby zakonczyc")
    wybor_uzytkownika = int(input('-'))
    if wybor_uzytkownika is 1:
         magazyn.wyswietl_dostepne_produkty()
    elif wybor_uzytkownika is 2:
         magazyn.dodaj_produkt()
    elif wybor_uzytkownika is 3:
         magazyn.usun_produkt()
    elif wybor_uzytkownika is 4:
         sys.exit()










            
