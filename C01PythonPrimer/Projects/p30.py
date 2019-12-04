def halvings(n):
    assert isinstance(n, int) and n >= 2, f"arg should be an integer >= 2, not {n}"
    return n.bit_length() - 1


if __name__ == "__main__":
    # Good
    n = 3
    print(n, halvings(n))
    n = 4
    print(n, halvings(n))
    n = 1000
    print(n, halvings(n))
    # Ungood
    try:
        halvings(3.7)
    except Exception as e:
        print(e)
    try:
        halvings(1)
    except Exception as e:
        print(e)
