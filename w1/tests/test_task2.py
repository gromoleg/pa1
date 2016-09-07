import unittest
from w1.task2 import sln
from w1.tests.data import test_data

method = 1  # see alignment methods, total: 3
"""
alignment methods:
0: 2**n
1: mod 2
2: no alignment
"""


class TestTask2(unittest.TestCase):
    def test_karatsuba(self):
        for xy, res in test_data.items():
            multiply_res, freq = sln(*xy)
            self.assertEqual(multiply_res, res[0])
            for k, v in res[1].items():
                self.assertEqual(freq[k], v[method])


if __name__ == '__main__':
    unittest.main()
