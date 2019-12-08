def evens_odds(l):
    def helper(index):
        if index == -1:
            return []
        if l[index] % 2 == 0:
            return [l[index]] + helper(index - 1)
        else:
            return helper(index - 1) + [l[index]]
    return helper(len(l) - 1)


if __name__ == "__main__":
    print(evens_odds([1, 2, 3, 4, 5, 6]))
