# Note that it is also possible to solve it in O(n) time (and with less pain) using sets, I think.

from math import inf


def merge_and_reverse(a, b, c):  # The reverse is not useful but easier to do
    result = []
    while a or b or c:
        va = a[-1] if a else -inf
        vb = b[-1] if b else -inf
        vc = c[-1] if c else -inf
        if va >= vb and va >= vc:
            result.append(a.pop())
        elif vb >= vc:
            result.append(b.pop())
        else:
            result.append(c.pop())
    return result


def disjoint(a, b, c):
    # Create merged list
    sa = sorted(a)
    sb = sorted(b)
    sc = sorted(c)
    m = merge_and_reverse(sa, sb, sc)  # This destroys sa, sb and sc in the process
    # Use it
    for i in range(len(m) - 2):
        if m[i] == m[i + 1] == m[i + 2]:
            return False
    return True


if __name__ == "__main__":
    # Test merge
    print(merge_and_reverse([1, 4, 7], [2, 3, 8], [5, 6, 9]))

    # False
    a = [1, 2, 3]
    b = [2, 3, 4]
    c = [3, 4, 5]
    print(disjoint(a, b, c))
    # True
    a = [1, 2]
    b = [2, 3, 4]
    c = [3, 4, 5]
    print(disjoint(a, b, c))
