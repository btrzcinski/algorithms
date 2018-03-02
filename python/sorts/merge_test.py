import random
import unittest

import merge

class MergeSortTests(unittest.TestCase):

    def setUp(self):
        self.input = list(range(10))

    def test_random(self):
        random.shuffle(self.input)
        
        actual = merge.sort(self.input)
        self.assertEqual(list(sorted(actual)), actual)

    def test_sorted(self):
        actual = merge.sort(self.input)
        self.assertEqual(list(sorted(actual)), actual)

    def test_oneoff(self):
        self.input[0], self.input[1] = self.input[1], self.input[0]

        actual = merge.sort(self.input)
        self.assertEqual(list(sorted(actual)), actual)

    def test_reversed(self):
        self.input.reverse()

        actual = merge.sort(self.input)
        self.assertEqual(list(sorted(actual)), actual)

if __name__ == '__main__':
    unittest.main()

        
        