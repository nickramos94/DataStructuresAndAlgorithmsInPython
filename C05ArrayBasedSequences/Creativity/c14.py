from collections import Counter
from random import randrange


def shuffle(lst):
    """O(n)
    Returns a new list, unlike the random.shuffle function which shuffles in place.
    """
    new = lst[:]
    for i in range(1, len(lst)):
        swap_index = randrange(0, i + 1)
        new[i], new[swap_index] = new[swap_index], new[i]
    return new


if __name__ == "__main__":
    # Wonderful code
    lst = list(range(10))
    indices_zero = []
    indices_four = []
    indices_nine = []
    for _ in range(100000):
        new = shuffle(lst)
        indices_zero.append(new.index(0))
        indices_four.append(new.index(4))
        indices_nine.append(new.index(9))
    print(Counter(indices_zero))
    print(Counter(indices_four))
    print(Counter(indices_nine))
