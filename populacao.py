import random


class Populacao:

    def __init__(self):
        self._elem = []

    def add(self, individuo):
        self._elem.append(individuo.getId(), individuo)
        # Fazer binary search para encontrar k
        self._elem.insert(k, individuo)

    def replace(self, id, individuo):
        # Pesquisa binária para encontrar individuo
        self._elem[id] = individuo
        
    def getIndividuo(self, id):
        return self._elem[id]

    def getAll(self):
        return self._elem

    #Verificar bounds do range e meter no main
    def getRandomOther(self, id):
        r = random.randint(0, len(self._elem)-2)
        if r >= id:
            r += 1
        return self._elem[r]
        
