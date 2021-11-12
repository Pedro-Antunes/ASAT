import random


class Populacao:

    def __init__(self):
        self._elem = []

    def add(self, individuo):
        k = self._locate(individuo.getId())
        self._elem.insert(k, individuo)

    def replace(self, id, individuo):
        k = self._locate(id)
        self._elem[k] = individuo
        
    def getIndividuo(self, id):
        return self._elem[id]

    def getAll(self):
        return self._elem

    def getRandomOther(self, id):
        r = random.randint(0, len(self._elem)-2)
        if r >= id:
            r += 1
        return self._elem[r]

    def _locate(self, id):
        left = 0
        right = len(self._elem)
        while left < right:
            mid = (left + right) // 2
            if  id > self._elem[mid].getId():
                left = mid + 1
            else:
                right = mid
        return left
