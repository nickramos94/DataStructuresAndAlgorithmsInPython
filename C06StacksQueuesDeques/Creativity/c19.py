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


def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k].split()[0]  # Removes attributes
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k + 1)
    return S.is_empty()


if __name__ == "__main__":
    # True
    html = """
<html lang="kl">
    <head>
    </head>
    <body>
    </body>
</html>
"""
    print(is_matched_html(html))

    # False
    html = """
<html lang="kl">
    <head>
    </head>
    <body>
    </body>
</htmlol>
"""
    print(is_matched_html(html))
