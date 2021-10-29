class Heap:

    def __init__(self, comp=lambda a, b: a < b):
        self.tree = [None]
        self.comp = comp

    def push(self, object):
        self.tree.append(object)
        self.siftUp(len(self.tree) - 1)
        return

    def pop(self):
        top = self.tree[1]
        self.tree[1] = self.tree[-1]
        self.tree.pop()
        self.siftDown(1)
        return top

    def top(self):
        return self.tree[1]

    def replace(self, object):
        top = self.tree[1]
        self.tree[1] = object
        self.siftDown(1)
        return top

    def siftUp(self, node):
        while node != 1 and self.comp(self.tree[node // 2], self.tree[node]):
            self.swap(node, node // 2)
            node //= 2

    def siftDown(self, node):
        while node * 2 + 1 < len(self.tree) and (self.comp(self.tree[node], self.tree[node * 2]) or self.comp(self.tree[node], self.tree[node * 2 + 1])):
            if self.comp(self.tree[node * 2], self.tree[node * 2 + 1]):
                self.swap(node, node * 2 + 1)
                node = node * 2 + 1
            else:
                self.swap(node, node * 2)
                node *= 2

    def swap(self, i, j):
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]

    def show(self):
        line = ""
        for i in range(1, len(self.tree)):
            line += f"{self.tree[i]} "
            if not (i+1)&i:
                print(line)
                line = ""
        print(line)