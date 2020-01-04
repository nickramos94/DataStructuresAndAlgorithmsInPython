# Comprehension is faster than generator, somehow.
# The rest is expected.

from time import time

SIZE = 100000


def test_append():
    result = []
    for _ in range(SIZE):
        result.append("f")
    return "".join(result)


def test_comprehension():
    return "".join(["f" for _ in range(SIZE)])


def test_concat():
    result = ""
    for _ in range(SIZE):
        result += "f"
    return result


def test_generator():
    return "".join("f" for _ in range(SIZE))


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
