from .data import DataReader


class Solution(object):
    def __init__(self, name, data=None):
        self.name = name
        self.data = data or DataReader(name)

    def get_inversions(self, user1, user2):
        if self.data.input is None:
            self.data.read()
        d1, d2 = self.data.input[user1], self.data.input[user2]
        d2 = sorted(d2, key=lambda x: d1[d2.index(x)])
        return sum(sum(d2[x] > y for y in d2[x + 1:]) for x in range(len(d2) - 1))
