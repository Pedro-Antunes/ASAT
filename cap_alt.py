class CAP:

    def __init__(self):
        self._eventList = []

    def add(self, evento):
        left = 0
        right = len(self._eventList)
        while left < right:
            mid = (left + right) // 2
            if evento.getTime() > self._eventList[mid].getTime():
                right = mid
            else:
                left = mid + 1
        self._eventList.insert(left, evento)

    def next(self):
        return self._eventList[-1]

    def remove(self):
        self._eventList.pop()
