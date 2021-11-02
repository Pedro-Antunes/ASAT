class Bitset:
    
    def __init__(self):
        self.data = 0
        self.trueBits = 0
    
    def set(self, i):
        self.data |= 1<<i
        
    def reset(self, i):
        self.data &= ~(1<<i)
            
    def flip(self, i):
        self.data ^= 1<<i
        
    def get(self, i):
        # TA A DAR BUG AQUI PLS HELP
        print(type(self.data), type(1 << i))
        return bool(self.data & (1 << i))

    def count(self):
        pass