class Bitset:

    def __init__(self, size):
        self._data = [0]*size
        self._size = size

    def getSize(self):
        return self._size

    def set(self, i):
        self._data[i] = 1
        
    def reset(self, i):
        self._data[i] = 0
            
    def flip(self, i):
        if self._data[i] == 0:
            self._data[i] = 1
        else:
            self._data[i] = 0
        
    def test(self, i):
        return bool(self._data[i])

    def count(self):
        c = 0
        for i in range(self._size):
            if self.test(i):
                c += 1
        return c
