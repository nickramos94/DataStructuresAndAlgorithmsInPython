lines = []
while True:
    try:
        new = input("SAY SOMETHING ")
        assert new != ""
        lines.append(new)
    except:
        print()
        print("\n".join(lines[::-1]))
        break
