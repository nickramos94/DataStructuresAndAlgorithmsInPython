def alphabetize(s):
    return " ".join("".join(c for c in s if c.isalnum() or c == " ").split())


if __name__ == "__main__":
    s = "Let's try, Mike."
    print(alphabetize(s))
    s = "Je m'appelle Haksell ! Et toi ?"
    print(alphabetize(s))
