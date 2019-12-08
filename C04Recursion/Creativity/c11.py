def unique(l):
    # Pretty bad
    # We'll juste assume that in is recursive to because lazy
    def helper(high):
        if high == 0:
            return True
        return helper(high - 1) and (l[high] not in l[:high])
    return helper(len(l) - 1)


if __name__ == "__main__":
    from random import randint
    # Should output nothing
    for _ in range(1000):
        l = [randint(0, 100) for i in range(10)]
        bool_sure = len(l) == len(set(l))
        bool_test = unique(l)
        if bool_sure != bool_test:
            print(l, "should be", bool_sure, "but is", bool_test)
