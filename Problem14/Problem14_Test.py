from Problem14 import *
import unittest

class TestProblem14(unittest.TestCase): 
  def test_problem14(self): 
      self.assertEqual(lcp(["flower", "flow", "flight"]), "fl", "Should be 'fl'.") 
      self.assertEqual(lcp(["dog", "racecar", "car"]), "", "Should be ''.") 
      
if __name__ == '__main__': 
    unittest.main()
    
