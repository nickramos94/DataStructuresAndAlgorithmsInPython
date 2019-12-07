def poly_stupid(a, x):
    """O(n log n) with recursive power, O(n^2) with stupid power"""
    total = 0
    for i, e in enumerate(a):
        total += e * x ** i
    return total


def poly_better(a, x):
    """O(n)"""
    total = 0
    power = 1
    for e in a:
        total += e * power
        power *= x
    return total


def poly_horner(a, x):
    """O(n)"""
    total = a[-1]
    for e in a[-2::-1]:
        total *= x
        total += e
    return total


if __name__ == "__main__":
    a = [1, 4, 7, 4]  # 1 + 4x + 7x^2 + 4x^3
    print(poly_stupid(a, 2))
    print(poly_better(a, 2))
    print(poly_horner(a, 2))
