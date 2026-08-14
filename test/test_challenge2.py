import unittest
import challenge2

class Test_Challenge2(unittest.TestCase):
    def setUp(self):
        self.arr = [4, 7, 8, 2, 5, 10, 15, 20, 21, 16, 19]

    def test_bubble_sort(self):
        result = challenge2.bubble_sort(self.arr)
        self.assertEqual(result, [2, 4, 5, 7, 8, 10, 15, 16, 19, 20, 21])

    def test_selection_sort(self):
        result = challenge2.selection_sort(self.arr)
        self.assertEqual(result, [2, 4, 5, 7, 8, 10, 15, 16, 19, 20, 21])
            
    def test_insertion_sort(self):
        result = challenge2.insertion_sort(self.arr)
        self.assertEqual(result, [2, 4, 5, 7, 8, 10, 15, 16, 19, 20, 21])

if __name__ == '__main__':
    unittest.main()