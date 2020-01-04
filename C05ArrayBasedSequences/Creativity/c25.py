from random import randrange


def remove_all(lst, value):
    # Far from optimal but still O(n)
    lst[:] = [e for e in lst if e != value]


if __name__ == "__main__":
    lst = [randrange(10) for _ in range(100)]
    print(lst)
    print(len(lst))
    remove_all(lst, 6)
    print(lst)
    print(len(lst))
