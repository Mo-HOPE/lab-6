import unittest
from function import add

class test_add_function(unittest.TestCase):
  def test_add(self):
    
    self.assertEqual(add(5, 5), 10)
    self.assertEqual(add(-2, 3), 1)
    self.assertEqual(add(100, 0), 100)

if __name__ == '__main__':
    unittest.main()
