"""
Not a pretty or full-fledged implentation.
More of a proof of concept.
A recursive implementation is left to the reader.

For each pair of numbers, put the smallest in minis and the biggest in maxis (n/2)
For each pair in minis, put the smallest in a new list. Do the same for maxis (n/2)
Find the min of new_minis and the max of new_maxis (< n/2)
"""

from random import randint


def minmax(l):
    # Only works when the size of the input is a multiple of 4.
    COMPARAISONS = 0  # Not part of the alg, juste here to show that we are sub 3n/2
    maxis = []
    minis = []
    # Divide once
    for a, b in zip(l[::2], l[1::2]):
        COMPARAISONS += 1
        if a > b:
            maxis.append(a)
            minis.append(b)
        else:
            maxis.append(b)
            minis.append(b)
    # Divide the minis
    new_minis = []
    for a, b in zip(minis[::2], minis[1::2]):
        COMPARAISONS += 1
        if a > b:
            new_minis.append(b)
        else:
            new_minis.append(b)
    # Find the min
    mini = new_minis[0]
    for e in new_minis[1:]:
        COMPARAISONS += 1
        if e < mini:
            mini = e
    # Dive the maxis
    new_maxis = []
    for a, b in zip(maxis[::2], maxis[1::2]):
        COMPARAISONS += 1
        if a > b:
            new_maxis.append(b)
        else:
            new_maxis.append(b)
    # Find the max
    maxi = new_maxis[0]
    for e in new_maxis[1:]:
        COMPARAISONS += 1
        if e > maxi:
            maxi = e
    # Return
    return mini, maxi, COMPARAISONS


if __name__ == "__main__":
    # Basic list
    l = [3, 7, 9, 1, 2, 23, 4, -9]
    print(*minmax(l))
    # Each new element is either a min or a max
    l = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, 6, 7, 8, 9, 10, 11]
    print(*minmax(l))
    # Random list
    l = [randint(0, 1000000) for i in range(1000)]
    print(*minmax(l))
