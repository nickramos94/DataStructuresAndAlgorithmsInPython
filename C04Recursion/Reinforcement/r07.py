from random import randint


def str_to_int(s):
    def helper(result, index):
        if index == len(s):
            return result
        return helper(10 * result + ord(s[index]) - 48, index + 1)
    return helper(0, 0)


if __name__ == "__main__":
    for _ in range(10):
        n = randint(0, 1000)
        print(n, str_to_int(str(n)))
