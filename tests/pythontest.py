import unittest

class PyUnitTestCases(unittest.TestCase):

  def test_01_case01(self):
    print """this is the first test case"""

  def test_02_case02(self):
    print """this is the second case"""

if __name__ == '__main__':
  unittest.main()
