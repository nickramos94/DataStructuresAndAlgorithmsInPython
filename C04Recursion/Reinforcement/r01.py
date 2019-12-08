"""
Running time : O(n), we reduce high by 1 in each iteration.
Space : O(n) due to recursion stack.
---
Where I found the term "init" : http://s3.amazonaws.com/lyah/listmonster.png
"""

from random import randint


def max_recursive(l):
    def helper(high):
        if high == 0:
            return l[0]
        max_init = helper(high - 1)
        if l[high] > max_init:
            return l[high]
        else:
            return max_init
    return helper(len(l) - 1)


if __name__ == "__main__":
    # Should print nothing
    for i in range(10000):
        l = [randint(0, 1000000) for i in range(100)]
        my_max = max_recursive(l)
        true_max = max(l)
        if my_max != true_max:
            print(l, my_max, true_max)
