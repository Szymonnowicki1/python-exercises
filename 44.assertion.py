# -*- coding: utf-8 -*-

#%%
"""
assertEquel = sprawdza czy 2 elementy sa rowne
assertNotEquel = sprawdza czy 2 elementy nie sa rowne
assertTrue = sprawdza czy element jest prawda
assertFalse = sprawdza czy element jest falszem
assertIn = sprawdza czy element nalezy
assertNotIn = sprawdza czy element nie nalezy
"""

# %%
import unittest

class SimpleTest(unittest.TestCase):
    
    
    def test_add(self):
        self.assertEquel(3 + 5, 8)
        
    def test_sub(self):
        self.assertNotEquel(3 - 1, 1)
        
    def test_true(self):
        self.assertTrue(3 + 2 == 5)
        
    def test_false(self):
        self.assertFalse(3 + 5 == 1)
        
    def test_in(self):
        self.assertIn(1 , [1, 2, 3, 4])
        
    def test_not_in(self):
        self.assertNotEquel(6, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()

# %%















