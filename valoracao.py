from bitset import Bitset


class Valoracao(Bitset):

    def __init__(self, N):
        super().__init__(N)

    def display(self):
        s = ""
        for i in range(self.getSize()):
            if self.test(i):
                s += "1"
            else:
                s += "0"
        return s
