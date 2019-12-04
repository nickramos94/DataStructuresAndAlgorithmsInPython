from random import choice, randrange
from string import printable

possible_typos = ["substitution", "deletion", "insertion", "swap"]
punition = "I will never spam my friends again."
text = "".join(f"{i:02} : {punition}\n" for i in range(100))
text = list(text)

for _ in range(8):
    typo = possible_typos[randrange(4)]
    if typo == "substitution":
        typo_index = randrange(len(text))
        text[typo_index] = choice(printable)
    elif typo == "deletion":
        typo_index = randrange(len(text))
        del text[typo_index]
    elif typo == "insertion":
        typo_index = randrange(len(text) + 1)
        text.insert(typo_index, choice(printable))
    elif typo == "swap":
        typo_index = randrange(len(text) - 1)
        text[typo_index], text[typo_index + 1] = text[typo_index + 1], text[typo_index]

print("".join(text))
