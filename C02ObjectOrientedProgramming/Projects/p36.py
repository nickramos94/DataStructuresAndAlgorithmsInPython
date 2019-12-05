"""No OOP.
No bear reproduction.
With 10 fishes at the start, the battle seems pretty even.
5 wins for bears and 5 wins for fishes in 10 experiments."""

from colorama import Fore, Style
import os
from random import randint, sample
import sys
from time import sleep

# Arguments (number of fished and speed mode)
try:
    assert 2 <= len(sys.argv) <= 3
    start_fishes = int(sys.argv[1])
    if len(sys.argv) == 3 and "fast" in sys.argv[2]:
        delay = False
    else:
        delay = True
except:
    print("Usage : python3 p36.py number_of_fishes [-fast]")
    print("Example : python3 p36.py 12 -fast")
    sys.exit()

# Constants
size = 20
n_bears = 8

# Initialize zoo
bears = set(sample(range(size * size), n_bears))
fishes = set(sample(range(size * size), start_fishes)) - bears
# 1D to 2D location (69 -> (3, 9))
bears = {(xy % size, xy // size) for xy in bears}
fishes = {(xy % size, xy // size) for xy in fishes}

while True:
    # Clear terminal
    os.system("cls" if os.name == "nt" else "clear")
    # Move bears
    new_bears = set()
    for bear in set(bears):  # Copy since we change it
        new_x, new_y = bear
        new_x = min(max(new_x + randint(-1, 1), 0), size - 1)  # constrain x
        new_y = min(max(new_y + randint(-1, 1), 0), size - 1)  # constrain y
        if (new_x, new_y) in bears or (new_x, new_y) in new_bears:
            new_bears.add(bear)
        else:
            new_bears.add((new_x, new_y))
        bears.remove(bear)
    bears = new_bears
    # Move fishes
    new_fishes = set()
    for fish in set(fishes):  # Copy since we change it
        new_x, new_y = fish
        new_x = min(max(new_x + randint(-1, 1), 0), size - 1)  # constrain x
        new_y = min(max(new_y + randint(-1, 1), 0), size - 1)  # constrain y
        candidate_fish = (new_x, new_y)
        if candidate_fish not in bears:
            if (candidate_fish != fish) and (candidate_fish in fishes or candidate_fish in new_fishes):
                new_fishes.add(fish)  # Behold the cycle of life
            new_fishes.add(candidate_fish)
        fishes.remove(fish)
    fishes = new_fishes
    # Print lake
    for y in range(size):
        line = []
        for x in range(size):
            if (x, y) in fishes:
                line.append(f"{Fore.GREEN}o{Style.RESET_ALL}")
            elif (x, y) in bears:
                line.append(f"{Fore.RED}B{Style.RESET_ALL}")
            else:
                line.append("~")
        print(" ".join(line))
    # Slow down animation
    if delay:
        sleep(0.1)
