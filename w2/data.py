class DataReader(object):
    def __init__(self, name):
        self.name = name
        self.input = None
        self.output = None
        self.users = self.films = None

    def read(self, read_output=False):
        def readline():
            while True:
                result = f.readline()
                if not result:
                    return result
                result = result.strip()
                if result and not result.startswith('#'):
                    return [int(x) for x in result.split(' ')]

        with open(self.name, encoding='utf-8') as f:
            self.users, self.films = readline()
            self.input = {i: readline()[1:] for i in range(1, self.users + 1)}
            self.output = dict()
            if read_output:
                while True:
                    num = readline()
                    if not num:
                        break
                    num = num[0]
                    self.output[num] = {i + (i >= num): readline()[1] for i in range(1, self.users)}
