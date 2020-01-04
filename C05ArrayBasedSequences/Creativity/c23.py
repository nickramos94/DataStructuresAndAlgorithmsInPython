# Not the question but close enough.

from time import time

SIZE = 100000


def test_alias():
    l = []
    append = l.append
    for _ in range(SIZE):
        append(0)


def test_append():
    l = []
    for _ in range(SIZE):
        l.append(0)


def test_bracket():
    l = []
    for _ in range(SIZE):
        l += [0]


def test_comma():
    l = []
    for _ in range(SIZE):
        l += 0,


def test_comprehension():
    l = [0 for _ in range(SIZE)]


def test_extend():
    l = []
    for _ in range(SIZE):
        l.extend([0])


def test_times():
    l = [0] * SIZE


def test_insertend():
    l = []
    for _ in range(SIZE):
        l.insert(len(l), 0)


def test_static():
    l = [None] * SIZE
    for i in range(SIZE):
        l[i] = 0


if __name__ == "__main__":
    # Get all local functions
    functions = [f for f in dir() if f.startswith("test")]
    # Time
    times = {f: 0 for f in functions}
    for _ in range(100):
        for f in functions:
            t0 = time()
            exec(f + "()")
            t1 = time()
            times[f] += t1 - t0
    # Print out
    line = f"Size of list : {SIZE}"
    print(line)
    for k, v in sorted(times.items(), key=lambda e: e[1]):
        line = f"{k:18} : {v:.3f}ms"
        print(line)
