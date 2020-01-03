# It always assumes the size of the list will be constant (so no extra space)
# but switches to dynamic mode (with constant 9/8) when an item is appended to the list

import sys


def experiment(begin_size=0):
    data = [None] * begin_size
    last_size = None
    while len(data) < 1000:
        size = sys.getsizeof(data)
        if size != last_size:
            print(f"Length : {len(data):>4} | Size in bytes : {size:>5} | Byte per element : {size/len(data):.3f}")
            last_size = size
        data.append(None)


if __name__ == "__main__":
    for i in range(1, 1000, 42):
        print()
        print(i)
        experiment(i)
