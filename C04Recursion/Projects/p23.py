import os


def find(path, filename):
    def helper(path):
        for e in os.listdir(path):
            new_path = os.path.join(path, e)
            if e == filename:
                result.append(new_path)
            # Not elif because we might look for a dir
            # Ex : If we have usr/loca/usr/, we want to return both usr/ paths.
            if os.path.isdir(new_path):
                helper(new_path)
    result = []
    helper(path)
    return result


if __name__ == "__main__":
    print(find("../..", "r01.py"))
    print(find("../..", "Projects"))
