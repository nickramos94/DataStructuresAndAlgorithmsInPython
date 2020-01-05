class Empty(Exception):
    """You tried to access an element from an empty stack. You failed."""
    pass


class ArrayStack:
    def __init__(self, initial=None):
        self.__data = [] if initial == None else initial

    def __len__(self):
        return len(self.__data)

    def __repr__(self):
        return f"ArrayStack([{', '.join(str(e) for e in self.__data)}])"

    def is_empty(self):
        return len(self.__data) == 0

    def top(self):
        try:
            return self.__data[-1]
        except:
            raise Empty("Stack is empty.")

    def push(self, elem):
        self.__data.append(elem)

    def pop(self):
        try:
            return self.__data.pop()
        except:
            raise Empty("Stack is empty.")


def transfer(stack1, stack2):
    while not stack1.is_empty():
        stack2.push(stack1.pop())


if __name__ == "__main__":
    # Stack 1
    stack1 = ArrayStack()
    stack1.push(27)
    stack1.push(42)
    stack1.push(69)
    stack1.push(111)
    print(stack1)

    # Stack 2
    stack2 = ArrayStack([0, 1, 2, 3])
    print(stack2)

    # Transfer
    transfer(stack1, stack2)
    print(stack1)
    print(stack2)
