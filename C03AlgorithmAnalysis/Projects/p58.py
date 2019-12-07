"""
Plot of the four "unique" functions for different size inputs.
Please note that the lists are always unique.
For random input, depending on the frequencies of repetition,
unique1 might be much better than unique2.
...
I got carried away and compared the last three functions more toroughly. It seems that the easiest answer is by far the best (the only O(n)).
...
To revert to the true answer, replace
'for i in range(1, FUNCTIONS):' by 'for i in range(FUNCTIONS)'
and plt.plot by plt.loglog
Then remove the n and log n plot if you wish.
"""

import matplotlib.pyplot as plt
from random import randint
from time import time
from math import log2


def unique1(S):
    """O(n^2)"""
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True


def unique2(S):
    """O(n log n)"""
    temp = sorted(S)
    for j in range(1, len(temp)):
        if S[j-1] == S[j]:
            return False
    return True


def unique3(l):
    """O(n).. Or is it ? Seems to match perfectly with unique2. Maybe I don't understand sets after all."""
    setl = set()
    for e in l:
        if e in setl:
            return False
        setl.add(e)
    return True


def unique4(l):
    """O(n). Same doubts as with unique3."""
    return len(l) == len(set(l))


if __name__ == "__main__":
    FUNCTIONS = 4
    STEP = 10000
    TESTS = 40
    x = range(STEP, TESTS * STEP + 1, STEP)
    y = [[] for i in range(FUNCTIONS)]
    stop = [False] * FUNCTIONS
    for size in x:
        # Create the list (answer will always be True)
        a = set()
        while len(a) < size:
            a.add(randint(0, size * 2))
        a = list(a)
        # Time the functions
        for i in range(1, FUNCTIONS):
            if not stop[i]:
                t0 = time()
                exec(f"unique{i+1}(a)")
                t1 = time() - t0
                y[i].append(t1)
                if t1 > 1:
                    stop[i] = True
        print(size, "/", STEP * TESTS)  # TODO delete

    plt.xkcd()

    plt.plot(x, [n / 10000000 for n in x], label=f"n")
    plt.plot(x, [n * log2(n) / 80000000 for n in x], label=f"n log n")
    for i in range(1, FUNCTIONS):
        # The zip thing cuts off if x is longer than y.
        # Useful for unique1.
        plt.plot(*zip(*zip(x, y[i])), label=f"unique{i+1}")

    plt.xlabel("Size of input")
    plt.ylabel("Time to execute (s)")
    plt.legend()
    plt.show()
