from math import inf


def max_ten_sort(l):
    """This is O(n log n)."""
    return sorted(l, reverse=True)[:10]


def max_ten_loop(l):
    """This is O(n) with a big constant factor."""
    maxis = [-inf] * 10
    for e in l:
        if e > maxis[-1]:
            maxis.pop()
            i = 0
            while i < 9 and maxis[i] > e:  # Constant
                i += 1
            maxis.insert(i, e)  # Constant since maxis's size is fixed
    return maxis


if __name__ == "__main__":
    l = [i % 8 * i ** 2 for i in range(42)]
    print(l)
    print()
    print(max_ten_sort(l))
    print(max_ten_loop(l))
