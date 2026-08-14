import unittest
import challenge3

class Test_Challenge3(unittest.TestCase):
    def setUp(self):
        self.s = "MMXXV"
        
    def test_roman_to_integer(self):
        result = challenge3.roman_to_integer(self.s)
        self.assertEqual(result, 2025)
    
    def test_number_to_roman(self):
        result = challenge3.number_to_roman(2025)
        self.assertEqual(result, "MMXXV")

if __name__ == '__main__':
    unittest.main()