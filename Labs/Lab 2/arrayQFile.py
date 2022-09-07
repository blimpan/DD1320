from array import array


class ArrayQ:

    def __init__(self):
        self._queue = array("i")

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self._queue.pop(0)
        else:
            return False

    def size(self):
        return len(self._queue)

    def isEmpty(self):
        return self.size() == 0