def is_palindrome(s):
    def helper(low, high):
        if low >= high:
            return True
        return s[low] == s[high] and helper(low + 1, high - 1)
    return helper(0, len(s) - 1)


if __name__ == "__main__":
    # FFTT
    print(is_palindrome("abcd"))
    print(is_palindrome("abcda"))
    print(is_palindrome("abba"))
    print(is_palindrome("kayak"))
