from Problem01 import *
import unittest

class TestProblem01(unittest.TestCase): 
    def test_problem01(self): 
        self.assertEqual(twosum([2,7,11,15], 9), [0,1], "Should be [0,1]")
        self.assertEqual(twosum([3,2,4], 6), [1,2], "Should be [1,2]")
        self.assertEqual(twosum([3,3], 6), [0,1], "Should be [0,1]")

if __name__ == '__main__': 
    unittest.main()
