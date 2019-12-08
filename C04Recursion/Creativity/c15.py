def subsets(l):
    def helper(index, elems):
        if index == -1:
            print(elems)
        else:
            helper(index - 1, elems)
            helper(index - 1, [l[index]] + elems)
    helper(len(l) - 1, [])


if __name__ == "__main__":
    subsets([1, 2, 3, 4])
