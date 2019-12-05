from sys import argv

if len(argv) != 2:
    print("Usage : python3 p34.py file_name")
else:
    with open(argv[1]) as file:
        text = file.read()
    counter = dict()
    for c in text:
        counter[c] = counter.get(c, 0) + 1
    for k in sorted(counter.keys()):
        if not k.isspace():
            print(k * counter[k])
