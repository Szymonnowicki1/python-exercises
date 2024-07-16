# -*- coding: utf-8 -*-

class Student:
    
    lista_studentow = []
    
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.lista_studentow.append(self)
        
    @staticmethod
    def liczba_studentow():
        print('liczba studentow :', len(Student.lista_studentow))
        
# %%
student_1 = Student('jan', 'nowak', 17)
student_2 = Student('tomek', 'nowicki', 24)
student_3 = Student('adam', 'piesowka', 22)

# %%
Student.liczba_studentow()


# %%
classmethod