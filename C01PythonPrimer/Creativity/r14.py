def contains_odd_product(data):
    odd_count = 0
    for e in data:
        if e % 2 == 1:
            odd_count += 1
            if odd_count >= 2:
                return True
    return False


if __name__ == "__main__":
    data = [2, 4, 6, 8, 10]
    print(contains_odd_product(data))
    data = [6, 9]
    print(contains_odd_product(data))
    data = [2, 3, 5, 7, 11]
    print(contains_odd_product(data))
    data = [1, 3, 9, 25, 49]
    print(contains_odd_product(data))
