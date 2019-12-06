def all_distinct(data):
    return len(data) == len(set(data))


if __name__ == "__main__":
    # True
    data = [2, 4, 6, 8, 10]
    print(all_distinct(data))
    data = [6, 9]
    print(all_distinct(data))
    data = [2, 3, 5, 7, 11]
    print(all_distinct(data))
    data = [1, 3, 9, 25, 49]
    print(all_distinct(data))
    data = [0]
    print(all_distinct(data))
    data = []
    print(all_distinct(data))
    # False
    print()
    data = [0, 1, 1, 2, 3, 5]
    print(all_distinct(data))
    data = [7, 7, 7]
    print(all_distinct(data))
