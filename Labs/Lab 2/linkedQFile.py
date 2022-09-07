

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.isEmpty():
            pass
        else:
            item = self.first
            self.first = self.first.next
            return item.value

    def isEmpty(self):
        return self.first is None
