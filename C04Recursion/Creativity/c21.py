def pair_sum(l, value):
    def helper(low, high):
        if low >= high:
            return None
        add = l[low] + l[high]
        if add > value:
            return helper(low, high - 1)
        elif add < value:
            return helper(low + 1, high)
        else:
            return l[low], l[high]
    return helper(0, len(l) - 1)


if __name__ == "__main__":
    print(pair_sum([0, 1, 2, 3, 4, 7, 42, 69], 9))  # 2 7
    print(pair_sum([0, 1, 2, 3, 4, 7, 42, 69], 1))  # 0 1
    print(pair_sum([0, 1, 2, 3, 4, 7, 42, 69], 111))  # 42 69
    print(pair_sum([0, 1, 2, 3, 4, 7, 42, 69], 12))  # None
    print(pair_sum([0, 1, 2, 3, 4, 7, 42, 69], 14))  # None despite 7 + 7 = 14
