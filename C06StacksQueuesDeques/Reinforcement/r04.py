class Empty(Exception):
    """You tried to access an element from an empty stack. You failed."""
    pass


class ArrayStack:
    def __init__(self, initial=[]):
        self.__data = initial

    def __len__(self):
        return len(self.__data)

    def __repr__(self):
        return f"ArrayStack([{', '.join(str(e) for e in self.__data)}])"

    def is_empty(self):
        return len(self.__data) == 0

    def pop(self):
        try:
            return self.__data.pop()
        except:
            raise Empty("Stack is empty.")

    def push(self, elem):
        self.__data.append(elem)

    def remove_all(self):
        if self.is_empty():
            return
        else:
            self.pop()
            self.remove_all()

    def top(self):
        try:
            return self.__data[-1]
        except:
            raise Empty("Stack is empty.")


if __name__ == "__main__":
    stack = ArrayStack()
    stack.push(27)
    stack.push(42)
    stack.push(69)
    stack.push(111)
    print(stack)
    stack.remove_all()
    print(stack)
