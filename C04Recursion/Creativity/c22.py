def power(base, exp):
    """Confusing and uninspired on variable names, sorry."""
    result = 1
    div = 1
    cur = base
    while exp > 0:
        if div > exp:
            div = 1
            cur = base
            continue
        exp -= div
        div *= 2
        result *= cur
        cur *= cur
    return result


if __name__ == "__main__":
    print(power(2, 5))
    print(power(2, 6))
    print(power(2, 7))
    print(power(2, 8))
    print(power(3, 5))
