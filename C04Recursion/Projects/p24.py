"""
I suffered.
Takes about 22:27:00 to run on my computer.
"""


def algebra(*equations):
    def mappings(equation, rhaaa):
        letters = {c for c in equation if c.isalpha()}
        to_add = letters - rhaaa.keys()
        lhs, rhs = equation.split("=")
        # The iterative way of doing permutations
        for i in range(10 ** len(to_add)):
            candidate = dict(rhaaa)
            for j, c in enumerate(to_add):
                candidate[c] = (i // 10 ** j) % 10
            sum_lhs = sum(candidate.get(c, 0) for c in lhs)
            sum_rhs = sum(candidate.get(c, 0) for c in rhs)
            if sum_lhs == sum_rhs:
                yield candidate

    def helper(index, rhaaa):
        if index == 1:
            print(rhaaa)  # Checking where we are. It is long and lonely without.
        if index == len(equations):
            solutions.append(rhaaa)
            return
        for mapping in mappings(equations[index], rhaaa):
            helper(index + 1, mapping)

    solutions = []
    helper(0, dict())
    return solutions


if __name__ == "__main__":
    # print(algebra("a+a=b", "b+b=c", "a+b+b=d"))
    print(algebra("pot+pan=bib", "dog+cat=pig", "boy+girl=baby"))
