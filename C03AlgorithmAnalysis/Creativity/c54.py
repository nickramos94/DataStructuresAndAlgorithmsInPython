def mode(lst):
    """Doesn't even care about the range of values !"""
    # Create the dictionnary
    counter = dict()
    for e in lst:
        counter[e] = counter.get(e, 0) + 1
    # Find the most frequent value
    max_value = 0
    max_count = 0
    for n, count in counter.items():
        if count > max_count:
            max_count = count
            max_value = n
    return max_value


if __name__ == "__main__":
    print(mode([1, 2, 2, 2, 4, 3, 8, 7, 6]))
