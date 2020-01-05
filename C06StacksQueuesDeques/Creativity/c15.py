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

    def pop(self):
        try:
            return self.__data.pop()
        except:
            raise Empty("Stack is empty.")

    def push(self, elem):
        self.__data.append(elem)

    def clear(self):
        if self.is_empty():
            return
        else:
            self.pop()
            self.clear()

    def top(self):
        try:
            return self.__data[-1]
        except:
            raise Empty("Stack is empty.")


def maybe_max(stack):
    # Removes the top one
    top = stack.pop()
    return max(top, stack.top())


if __name__ == "__main__":
    stack = ArrayStack([1, 2, 3])
    print(maybe_max(stack))
    stack = ArrayStack([2, 3, 1])
    print(maybe_max(stack))
    stack = ArrayStack([3, 1, 2])
    print(maybe_max(stack))
