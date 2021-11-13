class Bitset:
    
    def __init__(self, size):
        self._data = [False]*size
        self._size = size

    def getSize(self):
        return self._size

    def st(self, i):
        self._data[i] = True
        
    def reset(self, i):
        self._data[i] = False
            
    def flip(self, i):
        self._data[i] = not self._data[i]
        
    def test(self, i):
        return self._data[i]

    def count(self):
        c = 0
        for i in range(self._size):
            if self.test(i):
                c += 1
        return c
