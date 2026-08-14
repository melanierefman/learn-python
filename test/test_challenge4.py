import unittest
import challenge4

class Test_Challenge4(unittest.TestCase):
    def setUp(self):
        self.x = 20
    
    def test_fibonacci(self):
        result = challenge4.fibonacci(self.x)
        self.assertEqual(result, 6765)
    
    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            challenge4.fibonacci(-5)
    
if __name__ == '__main__':
    unittest.main()