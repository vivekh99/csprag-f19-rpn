import unittest
#import numpy as np
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    #def test_dot_product(self):
     #   result = rpn.calculate("[[1,0], [0,1]] [[4,1]. [2,2]] @")
      #  self.assertEqual(np.array([[4,1], [2,2]]), result);
    def test_pow(self):
        result = rpn.calculate("1 2 ^")
        self.assertEqual(1, result)

if __name__ == '__main__':
    unittest.main()