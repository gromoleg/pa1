import unittest
from w1.task1 import karatsuba as sln
from w1.tests.data import test_data


class TestTask1(unittest.TestCase):
    def test_karatsuba(self):
        for xy, res in test_data.items():
            self.assertEqual(sln(*xy), res[0])


if __name__ == '__main__':
    unittest.main()
