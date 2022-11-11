import copy

from linkedQFile import LinkedQ


class Syntaxfel(Exception):

    def __init__(self, message="", point_of_error="", remaining_queue=LinkedQ()):
        self.message = message
        self.point_of_error = point_of_error
        self.remaining_queue = remaining_queue

    def __str__(self):
        return_str = self.message + " vid radslutet " + self.point_of_error + printQueue(self.remaining_queue)
        return return_str.strip()


def is_real_atom(an_atom):
    accepted_atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
                  'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br',
                  'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',
                  'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm',
                  'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
                  'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
                  'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

    return an_atom in accepted_atoms


def readFormula(q, s):
    readMolecule(q, s)
    if len(s) > 0:  # If there still is a starting parenthesis '(' in the stack at this point, we have a syntax error
        raise Syntaxfel("Saknad högerparentes")


def readMolecule(q, s):
    if q.peek() == ".":
        q.dequeue()
        return
    elif q.peek() == ")":  # If we get a ')' it means we are going back to readGroup()
        if len(s) > 0:  # If True, there is at least one '(' in the stack, which there should be
            s.pop()  # Remove one starting parenthesis
            q.dequeue()  # Remove the ending parenthesis
            readNum(q)
        else:
            raise Syntaxfel("Felaktig gruppstart", remaining_queue=q)
        return
    else:
        readGroup(q, s)
        if q.peek() == ".":
            pass
        else:
            readMolecule(q, s)
        return


def readGroup(q, s):
    if q.peek() == "(":  # A parenthesis would be the start of another molecule
        #print("Starting new molecule!")
        s.append("(")  # Add starting parenthesis to stack
        q.dequeue()  # Remove the starting parenthesis from the queue
        #print("readGroup() to readMolecule()")
        readMolecule(q, s)
        #print("Back from readMolecule() to readGroup()")

    else:
        readAtom(q)
        if nextIsNumber(q):
            readNum(q)
    return


def readAtom(q):
    if nextIsNumber(q):
        raise Syntaxfel("Felaktig gruppstart", remaining_queue=q)
    uppercase_letter = readLETTER(q)
    lowercase_letter = ""

    if nextIsNumber(q):
        pass
    elif not q.peek() == "." and q.peek().islower():
        lowercase_letter = readLetter(q)

    atom_symbol = uppercase_letter+lowercase_letter
    if is_real_atom(atom_symbol):
        return
    else:
        raise Syntaxfel("Okänd atom", remaining_queue=q)


def readLETTER(q):
    LETTER = q.dequeue()
    valid_values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    if LETTER in valid_values:
        return LETTER
    raise Syntaxfel("Saknad stor bokstav", LETTER, q)


def readLetter(q):
    letter = q.dequeue()
    #print("from readLetter: letter = " + letter)
    valid_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    if letter in valid_values:
        return letter
    else:
        raise Syntaxfel("Saknad liten bokstav", letter, q)


def readNum(q):
    number_as_str = q.dequeue()
    try:
        number_as_int = int(number_as_str)
        if number_as_int == 0:
            raise Syntaxfel("För litet tal", remaining_queue=q)
        if number_as_int == 1 and not nextIsNumber(q):
            raise Syntaxfel("För litet tal", remaining_queue=q)
        else:

            while type(number_as_int) is int:
                # This loop handles numbers until the next character isn't an integer.
                try:
                    number_as_int = int(q.peek())  # We test to see if the next character in the queue is also a number
                except ValueError:  # If it's not a number...
                    number_as_int = ""
                else:  # If it is a number...
                    number_as_str = q.dequeue()

    except ValueError:
        if number_as_str == ".":
            raise Syntaxfel("Saknad siffra", remaining_queue=q)
        else:
            raise Syntaxfel("Saknad siffra", number_as_str, q)


def printQueue(q):
    a_queue = copy.deepcopy(q)
    queue_as_str = ""
    if a_queue.isEmpty():
        return queue_as_str
    else:
        letter = a_queue.dequeue()
        while not letter == ".":
            queue_as_str += letter
            letter = a_queue.dequeue()
        return queue_as_str


def nextIsNumber(q):
    try:
        int(q.peek())
    except ValueError:  # next item is not a number
        return False
    else:
        return True


def checkParentheses(q):
    the_queue = copy.deepcopy(q)
    s = []  # We'll use a Python list as a stack for keeping track of parentheses.
    letter = the_queue.dequeue()
    while not letter == ".":
        try:
            if letter == "(":
                s.append(letter)
            elif letter == ")":
                if s[-1] == "(":  # If True, the parentheses match
                    s.pop()  # Remove a '(' from the stack
                else:  # If False, there is an unmatched parenthesis
                    raise Syntaxfel("Felaktig gruppstart", letter, the_queue)

            letter = the_queue.dequeue()
        except IndexError:
            raise Syntaxfel("Felaktig gruppstart", letter, the_queue)
    if len(s) > 0:  # If the list still contains an item after the entire queue has been checked, we have a syntax error
        raise Syntaxfel("Saknad högerparentes")
    return True


def storeSentence(word):
    q = LinkedQ()
    chars_list = [*word]
    for char in chars_list:
        q.enqueue(char)
    q.enqueue(".")
    return q


def check_syntax(word):
    q = storeSentence(word)
    try:
        # checkParentheses(q)
        pass
    except Syntaxfel as error:
        return str(error)

    s = []  # We'll use this as a stack for keeping track of parentheses
    try:
        readFormula(q, s)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as error:
        return str(error)


if __name__ == '__main__':
    user_input = ""
    input_list = []
    while True:
        user_input = input().strip().split(" ")
        if user_input[0] == "#":
            break
        else:
            input_list.append(user_input[0])

    for line in input_list:
        control_results = check_syntax(line)
        print(control_results)
