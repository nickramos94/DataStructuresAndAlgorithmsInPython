def repeated(lst):
    """O(n)"""
    return sum(lst) - (len(lst) * (len(lst) - 1)) // 2


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 4]
    print(repeated(lst))
    lst = [1, 2, 3, 4, 4, 5, 6, 7]
    print(repeated(lst))
