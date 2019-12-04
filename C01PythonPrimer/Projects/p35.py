from random import randrange

experiments = 1000

for people in range(5, 101, 5):
    collisions = 0  # Number of times at least two people share a birthday
    for _ in range(experiments):
        birthdays = [randrange(365) for i in range(people)]
        if len(set(birthdays)) != people:
            collisions += 1
    print(f"For {people:>3} people, two people share a birthday {collisions:>4} times out of {experiments} experiments.")
