from individuo import Individuo


class Populacao:

    def __init__(self, N_Individuo):
        self._elem = []
        self._h = 0
        for i in range(N_Individuo):
            self.add(Individuo(i))

    def add(self, ind):
        self._elem.append(ind)
        self._h += 1

    def remove(self, ind):
        return

    def getIndividuo(self, i):
        return self._elem[i]

    def getAll(self):
        return self._elem
