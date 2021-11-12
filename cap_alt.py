class CAP:

    def __init__(self):
        self._eventHeap = Heap(lambda evt1, evt2: evt1.getTime() > evt2.getTime())

    def add(self, evt):
        self._eventHeap.push(evt)

    def next(self):
        return self._eventHeap.top()

    def remove(self):
        self._eventHeap.pop()
