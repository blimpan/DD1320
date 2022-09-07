from arrayQFile import ArrayQ
from linkedQFile import LinkedQ
import unittest


def test_function():
    q = LinkedQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")


def magician_function():
    user_str = input("Enter a series of numbers (separated by space): ")
    str_list = user_str.split()
    int_list = [int(item) for item in str_list]

    pile = ArrayQ()
    for i in int_list:
        pile.enqueue(i)

    while not pile.isEmpty():
        # Until the queue is empty...
        # 1. pop the first item and put it last,
        # 2. pop the new first item and print it,
        # 3. repeat.

        pile.enqueue(pile.dequeue())
        print(pile.dequeue(), end=" ")

    print("\nQueue empty!")


# test_function()
magician_function()
# Number series for correct printout 7 1 12 2 8 3 11 4 9 5 13 6 10

"""
class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        #isEmpty ska returnera True för tom kö, False annars
        q = LinkedQ()
        self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
        q.enqueue(17)
        self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

    def test_order(self):
        #Kontrollerar att kö-ordningen blir rätt
        q = LinkedQ()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)


if __name__ == "__main__":
    unittest.main()
"""
