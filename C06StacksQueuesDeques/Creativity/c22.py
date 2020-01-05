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


def postfix_eval(expr):
    expr = expr.split()
    stack = ArrayStack()
    for elem in expr:
        if elem.isdigit():
            stack.push(elem)
        else:
            term2 = stack.pop()
            term1 = stack.pop()
            stack.push(eval(f"{term1}{elem}{term2}"))
    # Only return if stack length is one
    result = stack.pop()
    if stack.is_empty():
        return result
    else:
        raise ValueError


if __name__ == "__main__":
    expr = "5 2 + 8 3 - * 4 /"
    print(postfix_eval(expr))
