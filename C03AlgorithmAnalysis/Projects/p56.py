import matplotlib.pyplot as plt
from random import randint
from time import time


def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):             # loop from 0 to n-1
        total += S[j]
    return total


def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S)
    total = 0
    for j in range(0, n, 2):       # note the increment of 2
        total += S[j]
    return total


def example3(S):
    """Return the sum of the prefix sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):            # loop from 0 to n-1
        for k in range(1+j):        # loop from 0 to j
            total += S[k]
    return total


def example4(S):
    """Return the sum of the prefix sums of sequence S."""
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total


def example5(A, B):           # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prefix sums in A."""
    n = len(A)
    count = 0
    for i in range(n):          # loop from 0 to n-1
        total = 0
        for j in range(n):        # loop from 0 to n-1
            for k in range(1+j):    # loop from 0 to j
                total += A[k]
        if B[i] == total:
            count += 1
    return count


if __name__ == "__main__":
    FUNCTIONS = 5
    STEP = 100
    TESTS = 20
    x = range(STEP, TESTS * STEP + 1, STEP)
    y = [[] for i in range(FUNCTIONS)]
    stop = [False] * FUNCTIONS
    for size in x:
        a = [randint(0, 1000) for i in range(size)]
        b = [randint(0, 1000) for i in range(size)]
        for i in range(FUNCTIONS):
            if not stop[i]:
                t0 = time()
                if i == 4:
                    exec(f"example{i+1}(a, b)")
                else:
                    exec(f"example{i+1}(a)")
                t1 = time() - t0
                y[i].append(t1)
                if t1 > 1:
                    stop[i] = True

    plt.xkcd()

    for i in range(FUNCTIONS):
        plt.loglog(*zip(*zip(x, y[i])), label=f"example{i+1}")  # The zip thing cuts off if x is too long.

    plt.xlabel("Size of input")
    plt.ylabel("Time to execute (s)")
    plt.legend()
    plt.show()
