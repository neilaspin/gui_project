class Public:
    def __init__(self, number):
        self.number = number


    def __len__(self):
        return self.number


obj = Public(12,)
print(len(obj))

obj2 = Public(355)
print(len(obj2))