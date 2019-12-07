import matplotlib.pyplot as plt
from random import randint
from time import time


def prefix_average_1(lst):
    """O(n^2)"""
    answer = []
    for j in range(len(lst)):
        total = 0
        for i in range(j + 1):
            total += lst[i]
        answer.append(total / (j + 1))
    return answer


def prefix_average_2(lst):
    """O(n^2)"""
    answer = []
    for j in range(len(lst)):
        answer.append(sum(lst[:j+1]) / (j + 1))
    return answer


def prefix_average_3(lst):
    """O(n)"""
    answer = []
    total = 0
    for i, e in enumerate(lst):
        total += e
        answer.append(total / (i + 1))
    return answer


if __name__ == "__main__":
    step = 25
    x = range(step, 2001, step)
    y1 = []
    y2 = []
    y3 = []
    for size in x:
        l = [randint(0, 1000) for i in range(size)]
        # First one
        t0 = time()
        prefix_average_1(l)
        y1.append(time() - t0)
        # Second one
        t0 = time()
        prefix_average_2(l)
        y2.append(time() - t0)
        # Third one
        t0 = time()
        prefix_average_3(l)
        y3.append(time() - t0)

    plt.xkcd()

    plt.loglog(x, y1, label="prefix_average_1")
    plt.loglog(x, y2, label="prefix_average_2")
    plt.loglog(x, y3, label="prefix_average_3")

    plt.xlabel("Size of input")
    plt.ylabel("Time to execute (s)")
    plt.legend()
    plt.show()
