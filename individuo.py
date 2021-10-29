class Individuo:

    def __init__(self, id):
        self._id = id
        self._val = Valoracao()
        self._coef = 0
        self._mem = []
        self._actv = Valoracao()
        self._PrMut = 0.5

    def setVal(self, val):
        self._val = val

    def setCoef(self, value):
        self._coef = value

    def getId(self):
        return self._id
    
    def getVal(self):
        return self._val

    def getCoef(self):
        return self._coef

    def getPrMut(self):
        return self._PrMut

    def memorize(self, x):
        self._mem.append(x)

    def valCount(self):
        return len(self._mem)

    def uniqueValCount(self):
        pass
