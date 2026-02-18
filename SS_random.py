from random import *

class SS:
    def __init__(self, s = None):
        self.r = Random(s)

    def Random_integer(self, x, y):
        return self.r.randint(x, y)
    


#test
if __name__ == '__main__':
    r = SS()
    print(r.Random_integer(1, 10))
        