def sum_of_squares(n):
    assert isinstance(n, int) and n >= 0, f"sum_of_squares argument should be a positive integer, not {n}."
    return ((n - 1) * n * (2 * n - 1)) // 6


if __name__ == "__main__":
    try:
        print(sum_of_squares(4.23))
    except Exception as e:
        print(e)
    try:
        print(sum_of_squares(-7))
    except Exception as e:
        print(e)
    print(sum_of_squares(7))
    print(sum_of_squares(0))
    print(sum_of_squares(1234567))
    print(sum_of_squares(10**10000))
