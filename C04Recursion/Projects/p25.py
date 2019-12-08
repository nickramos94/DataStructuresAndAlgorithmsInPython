"""
Harder, you say ?
"""


def ruler_iterative(major_tick_length, size):
    ruler = "\n".join(f"{'-'*major_tick_length} {i}" for i in range(size + 1))
    for i in range(major_tick_length - 1, 0, -1):
        ruler = f"\n{'-'*i}\n".join(ruler.split("\n"))
    return ruler


if __name__ == "__main__":
    print(ruler_iterative(3, 2))
    print()
    print()
    print(ruler_iterative(4, 1))
