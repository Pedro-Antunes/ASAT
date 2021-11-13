class Formula:

    def __init__(self, path):
        self._varCount = 0
        self._clauseCount = 0
        self._columns = []
        clause = 0
        for line in open(path, "r"):
            if not line.startswith("c") and len(line) > 2:
                args = line.split()
                if args[0] == "p":
                    self._varCount = int(args[2])
                    self._clauseCount = int(args[3])
                    for _ in range(self._varCount):
                        self._columns.append([1 << self._clauseCount] * 2)
                else:
                    i = 0
                    while i < len(args) and args[i] != "0":
                        self._columns[abs(int(args[i])) - 1][int(int(args[i]) > 0)] |= (1 << clause)
                        i += 1
                    clause += 1

    def getVarCount(self):
        return self._varCount

    def getClauseCount(self):
        return self._clauseCount

    def evaluate(self, valoracao):
        orColumns = 1 << self._clauseCount  # Garante que tem o mesmo tamanho não sendo este bit usado
        for i in range(self._varCount):
            orColumns |= self._columns[i][valoracao.test(i)]
        satisfy = self._clauseCount
        while orColumns & (orColumns + 1):  # Só é falso quando orColumns = 111... base 2
            satisfy -= 1
            orColumns |= orColumns + 1  # Ativa o bit inativado menos significativo
        return satisfy

    def show(self):
        for i in range(len(self._columns)):
            print(f"{i}v")
            print(bin(self._columns[i][0]))
            print(bin(self._columns[i][1]))
