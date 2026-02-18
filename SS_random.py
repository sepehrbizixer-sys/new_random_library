from random import *

class SS:
    def __init__(self, s = None):
        self.r = Random(s)

    def Random_integer(self, x, y):
        return self.r.randint(x, y)
    
    def Choice_random_item(self, x):
        return self.r.choice(x)
    
    def rptint(self, seq):
        print(f'CPU : {seq}') #better to use for printing random items using this library
    


#test
if __name__ == '__main__':
    r = SS()
    print(r.Random_integer(1, 10))
    print(r.Choice_random_item(['ali', 'sepehr', 'masoomeh']))
    r.rptint(r.Random_integer(1, 10))
        