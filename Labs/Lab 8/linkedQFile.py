

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedQ:
    def __init__(self):
        self._first = None
        self._last = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node

    def dequeue(self):
        if self.isEmpty():
            pass
        else:
            item = self._first
            self._first = self._first.next
            return item.value

    def peek(self):
        return self._first.value

    def isEmpty(self):
        return self._first is None
