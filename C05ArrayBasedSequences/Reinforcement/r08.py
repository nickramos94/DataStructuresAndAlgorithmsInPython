# 0(n) for start and middle
# O(1) for end
# As expected

# Printing tables is hard

from time import time


def experiment(mode, size):
    lst = [None] * size
    while lst:
        if mode == "start":
            index = 0
        elif mode == "middle":
            index = len(lst) // 2
        elif mode == "end":
            index = len(lst) - 1
        lst.pop(index)


if __name__ == "__main__":
    size = 100
    times = {
        "start": [],
        "middle": [],
        "end": []
    }
    while size <= 100000:
        for mode in times:
            t0 = time()
            experiment(mode, size)
            t1 = time()
            times[mode].append(1000000 * (t1 - t0) / size)
        size *= 10
    print("           |   100 | 1000  | 10000 | 100000")
    print(f"k = 0      | {' | '.join(f'{e:.3f}' for e in times['start'])}")
    print(f"k = n // 2 | {' | '.join(f'{e:.3f}' for e in times['middle'])}")
    print(f"k = n      | {' | '.join(f'{e:.3f}' for e in times['end'])}")
