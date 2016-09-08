import unittest
import os
import glob
from w2.task import Solution
from w2.data import DataReader


class TestTask(unittest.TestCase):
    def test_inversions(self):
        for name in glob.glob(os.path.join(os.path.dirname(__file__), 'data_*.txt')):
            data = DataReader(name)
            data.read(read_output=True)
            sln = Solution(name, data)
            for user1 in data.output:
                inversions_data = data.output[user1]
                for user2 in inversions_data:
                    self.assertEqual(sln.get_inversions(user1, user2), inversions_data[user2])


if __name__ == '__main__':
    unittest.main()
