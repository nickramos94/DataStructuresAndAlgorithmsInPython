import os


def find(path, filename):
    if os.path.isdir(path):
        for e in os.listdir(path):
            if e == filename:
                print(os.path.join(path, e))
            else:
                find(os.path.join(path, e), filename)


if __name__ == "__main__":
    print(find("../../", "p01.py"))
    print(find(".", "p01.py"))
    print(find(".", "p23.py"))
