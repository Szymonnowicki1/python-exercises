# -*- coding: utf-8 -*-
# %%
import unittest

def div(x, y):
    return x / y


class RaiseTest(unittest.TestCase):
    
    def test_raise(self):
        self.assertRaises(ZeroDivisionError, div, 5, 0 )
    
if __name__ == '__main__':
    unittest.main()    













