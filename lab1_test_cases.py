#
# Test cases example for lab 1.
#

import unittest      # import the module that supports writing unit tests

# Define a class that will be used for these test cases.
# This class will include testing functions.
#
# Much of this code should be viewed as boilerplate for now.
#
class TestsLab1(unittest.TestCase):
   def test_expressions(self):         # Defines one testing function.
      self.assertEqual(0 + 1, 1)
   def test_expressions2(self):        # Defines a second testing function.
      self.assertEqual(2 * 2, 4)

   def test_expressions3(self):
      self.assertEqual(21 / 3, 7)

   def test_expressions4(self):
      self.assertAlmostEqual(21 / 3.0, 7.0)

   def test_expressions5(self):
      self.assertAlmostEqual(19 / 3, 6.3333333)

   def test_expressions6(self):
      self.assertEqual(19 // 3, 6)

   def test_expressions7(self):
      self.assertAlmostEqual(19 // 3.0, 6)

   def test_expressions8(self):
      self.assertAlmostEqual(4 * 2 + 27 / 3.0 + 4, 21.0)

   def test_expressions9(self):
      self.assertAlmostEqual(4 * (2 + 27) // 3 + 4, 42 )     

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

