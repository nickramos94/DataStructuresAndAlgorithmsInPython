def factors(n):
    # Start
    bigger_than_sqrt = []
    for i in range(1, int((n - 1) ** 0.5) + 1):
        if n % i == 0:
            bigger_than_sqrt.append(n // i)
            yield i
    # Middle
    sqrt = n ** 0.5
    if sqrt % 1 == 0:
        yield int(sqrt)
    # End
    for e in bigger_than_sqrt[::-1]:
        yield e


if __name__ == "__main__":
    for e in factors(42):
        print(e, "divides 42.")
    print()
    for e in factors(49):
        print(e, "divides 49.")
    print()
    for e in factors(4761):
        print(e, "divides 4761.")
