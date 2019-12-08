"""
isabel_sum([29, 98, 82, 15, 2, 81, 100, 3])
b = [127, 97, 83, 103]
return isabel_sum(b)
b = [224, 186]
return isabel_sum(b)
b = [410]
return 410

Seems to be O(n).
First time, we iterate over n elements.
Second time, we iterate over n//2 elements.
Third time, we iterate over n//4 elements.
...
In total, we iterate over 2n-1 elements.
"""


def isabel_sum(a):
    b = [a[2*i] + a[2*i+1] for i in range(len(a) // 2)]
    return b[0] if len(b) == 1 else isabel_sum(b)


if __name__ == "__main__":
    from random import randint
    for _ in range(10):
        l = [randint(0, 100) for _ in range(8)]
        print(l, sum(l), isabel_sum(l))
