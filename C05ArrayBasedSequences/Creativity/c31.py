def matrix_sum(matrix):
    def helper(n):
        if n == 0:
            return 0
        else:
            return sum(matrix[n - 1]) + helper(n - 1)
    return helper(len(matrix))


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(matrix_sum(matrix))
