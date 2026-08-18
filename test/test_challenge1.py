import unittest
import challenge1

class Test_Challenge1(unittest.TestCase):
    def setUp(self):
        self.arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        self.x = 23

    def test_linear_search_found(self):
        result = challenge1.linear_search(self.arr, self.x)
        self.assertEqual(result, 5)

    def test_linear_search_not_found(self):
        result = challenge1.linear_search(self.arr, 100)
        self.assertEqual(result, -1)

    def test_binary_search_found(self):
        result = challenge1.binary_search(self.arr, self.x)
        self.assertEqual(result, 5)

    def test_binary_search_not_found(self):
        result = challenge1.binary_search(self.arr, 100)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()