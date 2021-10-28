class Formula:

    def __init__(self):
        self.varCount = 0
        self.size = 0
        self.clauses = []

    def parse(self, path):
        self.varCount = 0
        self.size = 0
        self.clauses = []
        for line in open(path, "r"):
            if not line.startswith("c"):
                args = line.split()
                if args[0] == "p":
                    self.varCount = int(args[2])
                    self.size = int(args[3])
                else:
                    self.clauses.append([])
                    for literal in args:
                        if literal[0] == "-":
                            self.clauses[-1].append(-int(literal[1:]))
                        else:
                            self.clauses[-1].append(int(literal))

