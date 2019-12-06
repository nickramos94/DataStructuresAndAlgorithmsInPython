def correct(a, b, c):
    return a + b == c or a - b == c or a * b == c


if __name__ == "__main__":
    # True
    print(correct(2, 2, 4))
    print(correct(27, 42, 69))
    print(correct(1, 1, 1))
    # False
    print()
    print(correct(2, 2, 2))
    print(correct(17, 2, 49))
