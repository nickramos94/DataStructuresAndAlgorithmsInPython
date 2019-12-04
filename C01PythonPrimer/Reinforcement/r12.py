from random import randrange


def choice(data):
    return data[randrange(len(data))]


if __name__ == "__main__":
    data = [1]
    print(choice(data))
    data = [1, 2]
    print(choice(data))
