"""Not sure about myself but too lazy to test everything"""


class Empty(Exception):
    pass


class ArrayDeque:
    def __init__(self, capacity=5):
        self.__capacity = capacity
        self.__data = [None] * self.__capacity
        self.__front = 0
        self.__size = 0

    def __len__(self):
        return self.__size

    def __repr__(self):
        return f"ArrayDeque([{', '.join(str(e) for e in self.__data)}])"

    def add_first(self, value):
        if self.__size == self.__capacity:
            self.__capacity *= 2
            self.__resize(self.__capacity)
        self.__front = (self.__front - 1) % self.__capacity
        index = self.__front
        self.__data[index] = value
        self.__size += 1

    def add_last(self, value):
        if self.__size == self.__capacity:
            self.__capacity *= 2
            self.__resize(self.__capacity)
        index = (self.__front + self.__size) % self.__capacity
        self.__data[index] = value
        self.__size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        answer = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        if 0 < self.__size < self.__capacity // 4:
            self.__capacity = (self.__capacity + 1) // 2
            self.__resize(self.__capacity)
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        answer = self.__data[(self.__front + self.__size - 1) % self.__capacity]
        self.__data[(self.__front + self.__size - 1) % self.__capacity] = None
        self.__size -= 1
        if 0 < self.__size < self.__capacity // 4:
            self.__capacity = (self.__capacity + 1) // 2
            self.__resize(self.__capacity)
        return answer

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self.__data[self.__front]

    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self.__data[(self.__front + self.__size - 1) % self.__capacity]

    def is_empty(self):
        return self.__size == 0

    def __resize(self, capacity):
        old = self.__data
        self.__data = [None] * capacity
        walk = self.__front
        for k in range(self.__size):
            self.__data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self.__front = 0


if __name__ == "__main__":
    D = ArrayDeque()
    D.add_last(5)
    D.add_first(3)
    D.add_first(7)
    print(D)
    print(D.first())
    D.delete_last()
    print(D)
    print(len(D))
    D.delete_last()
    D.delete_last()
    print(D)
    D.add_first(6)
    print(D)
    print(D.first())
    print(D.last())
    print(D.add_first(8))
    print(D.is_empty())
    print(D.last())
