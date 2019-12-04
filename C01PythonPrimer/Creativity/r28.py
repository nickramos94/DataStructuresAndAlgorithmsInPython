def norm(vector, exp):
    return sum(n ** exp for n in vector) ** (1 / exp)


if __name__ == "__main__":
    vector = [3, 4]
    exp = 2
    print(vector, exp, norm(vector, exp))

    vector = [3, 4]
    exp = 3
    print(vector, exp, norm(vector, exp))

    vector = [2, 3, 5, 7, 11, 13]
    exp = 5
    print(vector, exp, norm(vector, exp))
