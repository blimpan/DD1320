from bintreeFile import Bintree
from linkedQFile import LinkedQ


def makeChildren(the_word):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    for i in range(len(the_word)):
        for letter in alfabet:
            modified_word = the_word[:i] + letter + the_word[i + 1:]
            if modified_word in svenska and modified_word not in gamla:
                q.enqueue(modified_word)
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
    q.enqueue(startord)

    while not q.isEmpty():
        word = q.dequeue()
        if word == slutord:
            print("Found a path to", slutord)
            exit()
        else:
            makeChildren(word)
    print("No path was found to", slutord)

