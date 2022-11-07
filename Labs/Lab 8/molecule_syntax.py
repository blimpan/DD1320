from linkedQFile import LinkedQ


class Syntaxfel(Exception):

    def __init__(self, message="", point_of_error=""):
        self.message = message
        self.point_of_error = point_of_error

    def __str__(self):
        return self.message + " vid radslutet " + self.point_of_error


def readMolecule(q):
    readAtom(q)
    #print("from readMolecule: peek = " + q.peek())
    if q.peek() == ".":
        q.dequeue()
    else:
        #print("Calling readNum now!")
        readNum(q)


def readAtom(q):
    readLETTER(q)
    #print("from readAtom: peek = " + q.peek())
    try:
        value = q.peek()
        int(value)
    except ValueError:
        #print("A letter can't be converted into an integer!")
        if not value == ".":
            readLetter(q)
    else:
        pass


def readLETTER(q):
    LETTER = q.dequeue()
    #print("from readLETTER: LETTER = " + LETTER)
    valid_values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    if LETTER in valid_values:
        return
    raise Syntaxfel("Saknad stor bokstav", LETTER)


def readLetter(q):
    letter = q.dequeue()
    #print("from readLetter: letter = " + letter)
    valid_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    if letter in valid_values:
        return
    raise Syntaxfel("Saknad liten bokstav", letter)


def readNum(q):
    try:
        #print("from readNum: peek = " + q.peek())
        number = q.dequeue()
        #print("from readNum: number = " + number)
        if int(number) == 0:
            raise Syntaxfel("För litet tal")
        if int(number) == 1 and q.peek() == ".":  # This checks whether we have another number after this one
            raise Syntaxfel("För litet tal")
            # We skip adding the variable number here in order to match the results from the lab instruction.
            # It doesn't really make sense to do it however...
        else:
            while not q.peek() == ".":
                # There should only be integers remaining, so we handle the remaining queue items here.
                number = q.dequeue()
                #print("from readNum: number = " + number)
                int(number)  # If there happens to be a non-integer at this point, we will raise an exception.
    except ValueError:
        raise Syntaxfel("Saknat tal")


def printQueue(q):
    queue_as_str = ""
    letter = q.dequeue()
    while not letter == ".":
        queue_as_str += letter
        letter = q.dequeue()
    return queue_as_str


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
        readMolecule(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as error:
        return str(error) + printQueue(q)


if __name__ == '__main__':
    user_input = ""
    input_list = []
    while True:
        user_input = input()
        if user_input == "#":
            break
        else:
            input_list.append(user_input)

    # print(input_list)

    for line in input_list:
        q = LinkedQ()
        control_results = check_syntax(line)
        print(control_results)
