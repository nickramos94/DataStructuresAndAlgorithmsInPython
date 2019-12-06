def dot(a, b):
    dotted = []
    for e1, e2 in zip(a, b):
        dotted.append(e1 * e2)
    return dotted


if __name__ == "__main__":
    a = [1, 3, 6, 10]
    b = [2, 3, 5, 7]
    dotted = dot(a, b)
    print(dotted, sum(dotted))
