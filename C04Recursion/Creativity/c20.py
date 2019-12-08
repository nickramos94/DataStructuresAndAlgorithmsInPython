def smalls_bigs(l, splt):
    """n O(n) calls (concatenating lists is painful) so O(n^2).
    Take my analysis with a grain of salt."""
    def helper(index):
        if index == -1:
            return []
        if l[index] <= splt:
            return [l[index]] + helper(index - 1)
        else:
            return helper(index - 1) + [l[index]]
    return helper(len(l) - 1)


if __name__ == "__main__":
    print(smalls_bigs([1337, 1, 12, 7, 6, 3, 42, 10, 69], 10))
