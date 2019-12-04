from random import randint


def shuffle(data):
    shuffled = data[:]
    n = len(data)
    for i in range(n):
        swap = randint(i, n - 1)
        shuffled[i], shuffled[swap] = shuffled[swap], shuffled[i]
    return shuffled


if __name__ == "__main__":
    # Big one
    data = list(range(15))
    print(data)
    data = shuffle(data)
    print(data)
    # Losts of small ones
    print()
    data = list(range(3))
    idems = sum(data == shuffle(data) for i in range(6000))
    print(f"{idems=} should be close to 1000.")
