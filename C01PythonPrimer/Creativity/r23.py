from random import randint

data = [1, 2, 7]
for i in range(10):
    try:
        n = randint(0, 5)
        print(data[n])
    except:
        print("Don’t try buffer overflow attacks in Python!")
