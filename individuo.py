class Individuo:

    def __init__(self, id):
        self.id = id
        self.val = Valoracao()
        self.mem = []
        self.actv = Valoracao()
        self.PrMut = 0.5

    def N_unique_val(self):
        return len(set(self.mem))
