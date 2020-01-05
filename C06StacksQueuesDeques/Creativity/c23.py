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

    def clear(self):
        if self.is_empty():
            return
        else:
            self.pop()
            self.clear()

    def is_empty(self):
        return len(self.__data) == 0

    def pop(self):
        try:
            return self.__data.pop()
        except:
            raise Empty("Stack is empty.")

    def push(self, elem):
        self.__data.append(elem)

    def reverse(self):
        # First stack (reversed)
        s1 = ArrayStack()
        while not self.is_empty():
            s1.push(self.pop())
        # Second stack (correct order)
        s2 = ArrayStack()
        while not s1.is_empty():
            s2.push(s1.pop())
        # Our stack (reversed)
        while not s2.is_empty():
            self.push(s2.pop())

    def top(self):
        try:
            return self.__data[-1]
        except:
            raise Empty("Stack is empty.")


if __name__ == "__main__":
    # Initialize
    stack1 = ArrayStack([1, 2, 3])
    stack2 = ArrayStack([4, 5])
    stack3 = ArrayStack([6, 7, 8, 9])
    # Switcharoo
    len2 = len(stack2)
    while not stack2.is_empty():
        stack1.push(stack2.pop())
    len3 = len(stack3)
    while not stack3.is_empty():
        stack1.push(stack3.pop())
    for _ in range(len3):
        stack2.push(stack1.pop())
    for _ in range(len2):
        stack2.push(stack1.pop())
    # Print
    print(stack1)
    print(stack2)
    print(stack3)
