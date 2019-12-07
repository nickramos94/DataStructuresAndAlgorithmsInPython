import matplotlib.pyplot as plt
from random import randint
from time import time
from math import log2


if __name__ == "__main__":
    STEP = 1000
    TESTS = 100
    x = range(STEP, TESTS * STEP + 1, STEP)
    y_sorted = []
    y_nlogn = []
    for size in x:
        a = [randint(0, 1000) for i in range(size)]
        t0 = time()
        sorted(a)
        t1 = time() - t0
        y_sorted.append(t1)
        y_nlogn.append(size * log2(size) / 100000000)

    plt.xkcd()

    plt.loglog(x, y_sorted, label=f"sorted")
    plt.loglog(x, y_nlogn, label=f"(n log2(n)) / 10^8")

    plt.xlabel("Size of input")
    plt.ylabel("Time to execute (s)")
    plt.legend()
    plt.show()
