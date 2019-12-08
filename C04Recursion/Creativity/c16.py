def recerse(s):
    def helper(low, high):
        if low == high:
            return s[low]
        if low > high:
            return ""
        return s[high] + helper(low + 1, high - 1) + s[low]
    return helper(0, len(s) - 1)


if __name__ == "__main__":
    print(recerse("abcdef"))
    print(recerse("abcdefg"))
