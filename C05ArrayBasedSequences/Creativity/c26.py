from collections import Counter
from random import shuffle


def find_repeating(lst):
    # O(n) so better than sorting and checking for equality with neighbors
    counter = Counter(lst)
    return [k for k, v in counter.items() if v > 1]


if __name__ == "__main__":
    lst = list(range(30)) + [3, 5, 8, 13, 21]
    shuffle(lst)  # Shuffles in-place
    print(find_repeating(lst))
