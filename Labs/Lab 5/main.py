from bintreeFile import Bintree
from linkedQFile import LinkedQ


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent


def writechain(final_node):
    if final_node is not None:
        writechain(final_node.parent)
        print(final_node.word)


def makeChildren(the_node):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    for i in range(len(the_node.word)):
        for letter in alfabet:
            modified_word = the_node.word[:i] + letter + the_node.word[i + 1:]
            if modified_word in svenska and modified_word not in gamla:
                new_node = ParentNode(modified_word, the_node)
                q.enqueue(new_node)
                gamla.put(modified_word)


if __name__ == "__main__":
    svenska = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as ordlista:
        for rad in ordlista:
            ordet = rad.strip()
            if ordet in svenska:
                pass
            else:
                svenska.put(ordet)

    startord = input("Enter initial word: ")
    slutord = input("Enter desired word: ")

    gamla = Bintree()
    gamla.put(startord)

    q = LinkedQ()
    start_node = ParentNode(startord)
    q.enqueue(start_node)

    while not q.isEmpty():
        a_node = q.dequeue()
        if a_node.word == slutord:
            print("Found a path to", slutord)
            writechain(a_node)
            exit()
        else:
            makeChildren(a_node)
    print("No path was found to", slutord)

