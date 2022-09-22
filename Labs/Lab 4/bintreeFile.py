class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

    def isParent(self):
        return self.left is not None or self.right is not None

    def isChild(self):
        return self.parent is not None

    def hasLeftChild(self):
        return self.left is not None

    def hasRightChild(self):
        return self.right is not None

    def isLeaf(self):
        return not self.hasRightChild() and not self.hasLeftChild()


class Bintree:

    def __init__(self):
        self.root = None

    def put(self, newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue)

    def __contains__(self, value):
        # True om value finns i trädet, False annars
        return finns(self.root, value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


def putta(the_root, a_value):
    new_node = Node(a_value)
    if the_root is None:
        return new_node
    elif the_root.value == a_value:
        print(a_value, "is already in the tree!")
    elif the_root.value < a_value:
        the_root.right = putta(the_root.right, a_value)
        the_root.right.parent = the_root
    elif the_root.value > a_value:
        the_root.left = putta(the_root.left, a_value)
        the_root.left.parent = the_root
    return the_root  # the function will end here for every call except for the first one


def finns(the_root, a_value):
    if the_root is None:
        return False
    elif the_root.value == a_value:
        return True
    else:
        return finns(the_root.left, a_value) or finns(the_root.right, a_value)


def skriv(the_node):

    if the_node is not None:
        skriv(the_node.left)
        print(the_node.value)  # Print the root
        skriv(the_node.right)

    """if the_node is None:
        print("Tree is empty!")
    else:
        if the_node.hasLeftChild():  # Go through the tree to the left first
            skriv(the_node.left)
            if the_node.isParent() and the_node.isChild():  # Don't print root node
                print(the_node.value)

        if the_node.isParent() and not the_node.isChild():  # After printing everything to the left, print root node
            print(the_node.value)

        if the_node.hasRightChild():  # Go through the tree to the right
            skriv(the_node.right)
            if the_node.isParent() and the_node.isChild() and not the_node.hasLeftChild():  # Don't print root node...
                # ... or the current node if it hasLeftChild() since it has already been printed then.
                print(the_node.value)

        if the_node.isLeaf():
            print(the_node.value)"""


def test_function():
    my_tree = Bintree()

    test_nums = [10, 5, 15, 1, 7, 6, 9, 8, 12, 11, 17]

    for num in test_nums:
        my_tree.put(num)
    for num in test_nums:
        print(num, my_tree.__contains__(num))
    print()
    my_tree.write()
