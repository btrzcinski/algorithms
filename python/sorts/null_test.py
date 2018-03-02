import random
import unittest

import null

class NullSortTests(unittest.TestCase):

    def setUp(self):
        self.actual = list(range(10))

    def test_random(self):
        random.shuffle(self.actual)
        expected = self.actual[:]
        
        null.sort(self.actual)
        self.assertEqual(expected, self.actual)

    def test_sorted(self):
        expected = self.actual[:]

        null.sort(self.actual)
        self.assertEqual(expected, self.actual)

    def test_oneoff(self):
        self.actual[0], self.actual[1] = self.actual[1], self.actual[0]
        expected = self.actual[:]

        null.sort(self.actual)
        self.assertEqual(expected, self.actual)

    def test_reversed(self):
        self.actual.reverse()
        expected = self.actual[:]

        null.sort(self.actual)
        self.assertEqual(expected, self.actual)
        
if __name__ == '__main__':
    unittest.main()
