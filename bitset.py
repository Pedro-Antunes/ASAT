import math


class Bitset:
    
    def __init__(self):
        self.data = 0

    def set(self, i):
        self.data |= 1<<i
        
    def reset(self, i):
        self.data &= ~(1<<i)
            
    def flip(self, i):
        self.data ^= 1<<i
        
    def test(self, i):
        return bool(self.data & 1<<i)

    def count(self):
        c = 0
        bits = self.data
        while bits:
            c += 1
            bits -= bits & -bits
        return c
