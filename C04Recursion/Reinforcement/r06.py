def reconic(n):
    if n == 1:
        return 1
    return 1 / n + reconic(n - 1)


if __name__ == "__main__":
    from math import log
    for n in range(1, 501):
        print(f"{reconic(n):.4f} {log(n):.4f}")
