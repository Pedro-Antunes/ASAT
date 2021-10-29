class Individuo:

    def __init__(self, identifier):
        self._id = identifier
        self._val = Valoracao()
        self._mem = []
        self._actv = Valoracao()
        self._PrMut = 0.5

    def getId(self):
        return self._id
    
    def getVal(self):
        return self._val

    def getPrMut(self):
        return self._PrMut

    def memorise(self, x):
        self._mem.append(x)

    def uniqueValCount(self):
        return len(set(self.mem))
