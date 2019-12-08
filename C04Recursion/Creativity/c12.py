def mult(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    partial = mult(a, b // 2)
    if b % 2 == 0:
        return partial + partial
    else:
        return a + partial + partial


if __name__ == "__main__":
    from random import randint
    # Should output nothing
    for _ in range(1000):
        a = randint(0, 1000)
        b = randint(0, 1000)
        if a * b != mult(a, b):
            print(a, b, a * b, mult(a, b))
