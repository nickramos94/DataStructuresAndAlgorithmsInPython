def missing(l):
    triangular = (len(l) + 1) * (len(l) + 2) // 2
    return triangular - sum(l)


if __name__ == "__main__":
    l = [1, 2, 5, 7, 6, 4]
    print(missing(l))
