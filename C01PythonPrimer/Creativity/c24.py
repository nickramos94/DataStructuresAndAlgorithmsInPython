VOWELS = {*"aeiouAEIOU"}


def count_vowels(s):
    return sum(c in VOWELS for c in s)


if __name__ == "__main__":
    s = "abcdef"
    print(s, count_vowels(s))
    s = "ABCDEF"
    print(s, count_vowels(s))
    s = "AEIOU"
    print(s, count_vowels(s))
    s = "BcDfG"
    print(s, count_vowels(s))
