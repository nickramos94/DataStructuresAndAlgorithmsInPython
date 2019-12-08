def minmax(l):
    def helper(index):
        if index == 0:
            return l[0], l[0]
        mini, maxi = helper(index - 1)
        if l[index] < mini:
            mini = l[index]
        if l[index] > maxi:
            maxi = l[index]
        return mini, maxi
    return helper(len(l) - 1)


if __name__ == "__main__":
    from random import randint
    for _ in range(10):
        l = [randint(0, 1000) for _ in range(10)]
        print(l)
        print(min(l), max(l), minmax(l))
        print()
