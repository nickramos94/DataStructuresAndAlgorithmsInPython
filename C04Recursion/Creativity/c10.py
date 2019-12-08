def truncated_log2(n):
    # Should probably output an error for n <= 0 but boring
    if n < 2:
        return 0
    return 1 + truncated_log2(n / 2)


if __name__ == "__main__":
    from math import log2
    # Should output nothing
    for n in range(1, 1001):
        if int(log2(n)) != truncated_log2(n):
            print(n, int(log2(n)), truncated_log2(n))
