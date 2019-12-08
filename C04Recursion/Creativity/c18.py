def conson_more(s):
    VOWELS = {*"aeiouAEIOU"}

    def consonants_minus_vowels(index):
        if index == -1:
            return 0
        count = -1 if s[index] in VOWELS else 1
        return count + consonants_minus_vowels(index - 1)

    return consonants_minus_vowels(len(s) - 1) > 0


if __name__ == "__main__":
    print(conson_more("abcde"))
    print(conson_more("abce"))
