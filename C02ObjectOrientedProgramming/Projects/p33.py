"""Only formats that work : nx^e, x^e, nx, x, n
All separated by +.
Example : 4x^3 + x^2 + 3x + 69"""


def parse_poly(poly):
    poly = "".join(c for c in poly.lower() if not c.isspace())
    terms = poly.split("+")
    poly_dict = dict()
    for term in terms:
        if "x" in term:
            if "^" in term:
                if term[0] != "x":
                    base, exp = term.split("^")
                    base = int(base[:-1])
                    exp = int(exp)
                    poly_dict[exp] = poly_dict.get(exp, 0) + base
                else:
                    exp = int(term[2:])
                    poly_dict[exp] = poly_dict.get(exp, 0) + 1
            else:
                if len(term) > 1:
                    poly_dict[1] = poly_dict.get(1, 0) + int(term[:-1])
                else:
                    poly_dict[1] = poly_dict.get(1, 0) + 1
        else:
            poly_dict[0] = poly_dict.get(0, 0) + int(term)
    return poly_dict


def derive_poly(poly):
    derived = dict()
    for k, v in poly.items():
        new = k * v
        if new:
            derived[k-1] = new
    return derived


def print_poly(poly):
    output = []
    for k in sorted(derived.keys(), reverse=True):
        if k == 0:
            output.append(f"{derived[k]}")
        elif k == 1:
            output.append(f"{derived[k]}x")
        else:
            output.append(f"{derived[k]}x^{k}")
    if output:
        print(" + ".join(output))
    else:
        print(0)


if __name__ == "__main__":
    while True:
        poly = input("Enter a polynomial : ")
        try:
            poly = parse_poly(poly)
            derived = derive_poly(poly)
            print_poly(derived)
        except Exception as e:
            print(e)
        print()
        print()
