
class HashNode:
    def __init__(self, key="", data=None, next=None):
        self.key = key
        self.data = data
        self.next = next


class Hashtable:
    def __init__(self, size):
        self.size = size
        self.list = [None] * self.size

    def store(self, key, data):
        hash_sum = self.hashfunction(key)
        node = HashNode(key, data)

        bottom_element = self.list[hash_sum]
        if bottom_element is None:
            self.list[hash_sum] = node
        else:
            node.next = self.list[hash_sum]
            self.list[hash_sum] = node
            """while bottom_element.next is not None:
                bottom_element = bottom_element.next
            bottom_element.next = node"""


    def search(self, key):
        hash_sum = self.hashfunction(key)

        top_element = self.list[hash_sum]
        while top_element is not None:
            if top_element.key == key:
                return top_element.data
            else:
                top_element = top_element.next
        raise KeyError

    def hashfunction(self, key):
        key_as_str = str(key)
        sum_of_chars = 0
        for c in key_as_str:
            sum_of_chars = sum_of_chars * 7919 + ord(c) * 4937  # two big prime numbers because it seems to work well

        return sum_of_chars % self.size



