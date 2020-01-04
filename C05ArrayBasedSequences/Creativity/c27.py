def find_missing(lst):
    elements = set(lst)  # O(n)
    candidate = min(lst) + 1  # O(n)
    while True:  # O(n)
        if candidate not in elements:
            return candidate
        candidate += 1


if __name__ == "__main__":
    lst = [8, 15, 12, 14, 9]
    print(find_missing(lst))
