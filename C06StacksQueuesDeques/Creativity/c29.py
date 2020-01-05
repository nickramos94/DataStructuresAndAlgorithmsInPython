class Empty(Exception):
    pass


class ArrayQueue:
    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__data = [None] * self.__capacity
        self.__front = 0
        self.__size = 0

    def __len__(self):
        return self.__size

    def __repr__(self):
        return f"ArrayQueue([{', '.join(str(e) for e in self.__data)}])"

    def dequeue(self):
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

    def enqueue(self, value):
        if self.__size == self.__capacity:
            self.__capacity *= 2
            self.__resize(self.__capacity)
        index = (self.__front + self.__size) % self.__capacity
        self.__data[index] = value
        self.__size += 1

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self.__data[self.__front]

    def is_empty(self):
        return self.__size == 0

    def rotate(self):
        self.__data[self.__front], self.__data[self.__front + self.__size] = None, self.__data[self.__front]
        self.__front += 1

    def __resize(self, capacity):
        old = self.__data
        self.__data = [None] * capacity
        walk = self.__front
        for k in range(self.__size):
            self.__data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self.__front = 0


if __name__ == "__main__":
    Q = ArrayQueue()
    print(Q)
    Q.enqueue(5)
    print(Q)
    Q.enqueue(3)
    print(Q)
    print(len(Q))
    Q.dequeue()
    print(Q)
    print(Q.is_empty())
    Q.dequeue()
    print(Q)
    print(Q.is_empty())
    try:
        Q.dequeue()
    except:
        print("EMPTY")
    print(Q)
    Q.enqueue(7)
    print(Q)
    Q.enqueue(9)
    print(Q)
    print(Q.first())
    Q.enqueue(4)
    Q.enqueue(4)
    Q.enqueue(4)
    Q.enqueue(4)
    Q.enqueue(4)
    Q.enqueue(4)
    Q.enqueue(4)
    Q.enqueue(4)
    Q.enqueue(4)
    Q.enqueue(4)
    print(Q)
    print(len(Q))
    Q.dequeue()
    Q.enqueue(2)
    print(Q)
    Q.rotate()
    Q.rotate()
    Q.rotate()
    print(Q)
