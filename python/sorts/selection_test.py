import random
import unittest

import selection

class SelectionSortTests(unittest.TestCase):

    def setUp(self):
        self.actual = list(range(10))

    def test_random(self):
        random.shuffle(self.actual)
        
        selection.sort(self.actual)
        self.assertEqual(list(sorted(self.actual)), self.actual)

    def test_sorted(self):
        selection.sort(self.actual)
        self.assertEqual(list(sorted(self.actual)), self.actual)

    def test_oneoff(self):
        self.actual[0], self.actual[1] = self.actual[1], self.actual[0]

        selection.sort(self.actual)
        self.assertEqual(list(sorted(self.actual)), self.actual)

    def test_reversed(self):
        self.actual.reverse()

        selection.sort(self.actual)
        self.assertEqual(list(sorted(self.actual)), self.actual)

if __name__ == '__main__':
    unittest.main()

        
        