import os


def walk(path):
    rhaaa = []
    dirnames = []
    filenames = []
    for e in os.listdir(path):
        new_path = os.path.join(path, e)
        if os.path.isdir(new_path):
            dirnames.append(e)
        else:
            filenames.append(e)
    yield((path, dirnames, filenames))
    for e in dirnames:
        new_path = os.path.join(path, e)
        yield from walk(new_path)  # New achievement unlocked


if __name__ == "__main__":
    for path in walk(".."):
        print(path)
    print()
    print()
    for path in os.walk(".."):
        print(path)
