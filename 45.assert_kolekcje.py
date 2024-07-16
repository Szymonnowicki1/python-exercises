# -*- coding: utf-8 -*-

# %%
"""
assertListEquel = sprawdza czy 2 listy sa rowne
assertTupleEquel = sprawdza czy 2 tuple sa rowne
assertSetEquel = sprawdza czy 2 zbiory sa rowne
assertDicEquel = sprawdza czy 2 slowniki sa rowne
"""

import unittest

class SimpleTest(unittest.TestCase):
    
    
    def test_1(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3])

    def test_2(self):
        self.assertTupleEqual((1, 2), (1, 2))

    def test_3(self):
        self.assertSetEqual({1, 2}, {1, 2})
        
    def test_4(self):
        self.assertDictEqual({'a' : 1}, {'a' : 1})
        
        
if __name__ == '__main__':
    unittest.main()

