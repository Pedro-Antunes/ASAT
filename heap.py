# DONE
class Heap:

    def __init__(self, comp=lambda a, b: a < b):
        self._tree = [None]
        self._comp = comp

    def push(self, object):
        self._tree.append(object)
        self.siftUp(len(self._tree) - 1)
        return

    def pop(self):
        top = self._tree[1]
        self._tree[1] = self._tree[-1]
        self._tree.pop()
        self.siftDown(1)
        return top

    def top(self):
        return self._tree[1]

    def replace(self, object):
        top = self._tree[1]
        self._tree[1] = object
        self.siftDown(1)
        return top

    def siftUp(self, node):
        while node != 1 and self._comp(self._tree[node // 2], self._tree[node]):
            self.swap(node, node // 2)
            node //= 2

    def siftDown(self, node):
        while node * 2 + 1 < len(self._tree) and (self._comp(self._tree[node], self._tree[node * 2]) or self._comp(self._tree[node], self._tree[node * 2 + 1])):
            if self._comp(self._tree[node * 2], self._tree[node * 2 + 1]):
                self.swap(node, node * 2 + 1)
                node = node * 2 + 1
            else:
                self.swap(node, node * 2)
                node *= 2

    def swap(self, i, j):
        self._tree[i], self._tree[j] = self._tree[j], self._tree[i]

    def show(self):
        line = ""
        for i in range(1, len(self._tree)):
            line += f"{self._tree[i]} "
            if not (i+1)&i:
                print(line)
                line = ""
        print(line)