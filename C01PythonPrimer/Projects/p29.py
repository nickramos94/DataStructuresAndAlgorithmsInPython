def permutations(data):
    n = len(data)
    assert n <= 12, f"{n}! is too much to handle."
    perms = []

    def recurations(perm, lst):
        if lst == []:
            perms.append(perm)
        else:
            for i, e in enumerate(lst):
                recurations(perm + [e], lst[:i] + lst[i+1:])
    recurations([], list(data))

    return perms


if __name__ == "__main__":
    from pprint import pprint
    print()
    pprint(permutations("abc"))
    print()
    pprint(permutations("catdog"))
    print()
    permutations("abcdefghijklmnopqrstuvwxyz")
