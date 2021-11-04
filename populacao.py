import random

from individuo import Individuo


class Populacao:

    def __init__(self):
        self._elem = []

    def create(self, val):
        self._elem.append(Individuo(len(self._elem), val))

    def colonize(self, id, individuo):
        self._elem[id] = individuo
        
    def getIndividuo(self, id):
        return self._elem[id]

    def getAll(self):
        return self._elem

    def getRandomOther(self, id):
        r = random.randint(0, len(self._elem)-2)
        if r >= id:
            r += 1
        return self._elem[r]
        
