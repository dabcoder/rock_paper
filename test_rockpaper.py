import unittest
import rockpaper

class TestComputersChoice(unittest.TestCase):

  def testReturnedCompValue(self):
  	vc = rockpaper.computers_choice()
  	self.assertGreaterEqual(vc, 1)
  	self.assertLessEqual(vc, 3)

if __name__ == '__main__':
  unittest.main()