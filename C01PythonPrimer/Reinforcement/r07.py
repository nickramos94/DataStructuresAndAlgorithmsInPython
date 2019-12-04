def sum_of_odd_squares(n):
    assert isinstance(n, int) and n >= 0, f"sum_of_squares argument should be a positive integer, not {n}."
    return sum(i ** 2 for i in range(1, n, 2))


if __name__ == "__main__":
    try:
        print(sum_of_odd_squares(4.23))
    except Exception as e:
        print(e)
    try:
        print(sum_of_odd_squares(-7))
    except Exception as e:
        print(e)
    for i in range(20):
        print(i, sum_of_odd_squares(i))
    print(sum_of_odd_squares(1234567))
