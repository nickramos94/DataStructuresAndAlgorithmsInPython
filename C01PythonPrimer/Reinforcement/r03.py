def minmax(data):
    if len(data) == 0:
        return None
    mini = maxi = data[0]
    for e in data[1:]:
        if e < mini:
            mini = e
        elif e > maxi:
            maxi = e
    return mini, maxi


if __name__ == "__main__":
    print(minmax([0, 4, 1, 3, 2]))
    print(minmax([7, 7, 7]))
    print(minmax([42]))
    print(minmax([]))
