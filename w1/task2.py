class KaratsubaMethod(object):
    def __init__(self, x, y):
        self.counter = dict()
        self.multiply_res = self.multiply(x, y)

    def multiply(self, x, y) -> int:
        """
        multiply x by y using Karatsuba method
        warning: recursion
        """
        if x < 10 and y < 10:
            return x * y
        x, y = str(x), str(y)
        n = max(len(x), len(y))
        if n % 2:
            n += 1
        x, y = x.zfill(n), y.zfill(n)
        a, b, c, d = int(x[:n // 2]), int(x[n // 2:]), int(y[:n // 2]), int(y[n // 2:])
        ac, bd = self.multiply(a, c), self.multiply(b, d)
        ad_bc = (self.multiply(a + b, c + d) - ac - bd)
        if ad_bc in self.counter:
            self.counter[ad_bc] += 1
        else:
            self.counter[ad_bc] = 1
        return (10 ** n) * ac + (10 ** (n // 2)) * ad_bc + bd


def sln(x, y):
    obj = KaratsubaMethod(x, y)
    return obj.multiply_res, obj.counter
