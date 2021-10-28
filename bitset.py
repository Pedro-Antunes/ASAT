class Bitset:
    
    def __init__(self):
        self.data = 0
    
    def set(self, i):
        self.data |= 1<<i
        
    def reset(self, i):
        self.data &= ~(1<<i)
    
    '''
    def set(self, i, val):
        self.reset(i)
        self.data |= int(val)<<i
    '''
        
        
    def flip(self, i):
        self.data ^= 1<<i
        
    def get(self, i):
        return bool(self.data & 1<<i)