class Bitset:
    
    def __init__(self, size):
        self._data = 0
        self._size = size

    def getSize(self):
        return self._size

    def set(self, i):
        self._data |= 1 << i
        
    def reset(self, i):
        self._data &= ~(1 << i)
            
    def flip(self, i):
        self._data ^= 1 << i
        
    def test(self, i):
        return bool(self._data & 1 << i)

    def count(self):
        c = 0
        bits = self._data
        while bits:
            c += 1
            bits -= bits & -bits
        return c
