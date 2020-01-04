def translate(string, shift):
    translated = ""  # I use repeated concatenation because I'm a madman
    for c in string:
        if c.isupper():
            translated += chr((ord(c) - ord("A") + shift) % 26 + ord("A"))
        elif c.islower():
            translated += chr((ord(c) - ord("a") + shift) % 26 + ord("a"))
        else:
            translated += c
    return translated


def encrypt(string, shift):
    return translate(string, shift)


def decrypt(string, shift):
    return translate(string, -shift)


if __name__ == "__main__":
    secret = "I like CHOCOLATE."
    encrypted = encrypt(secret, 3)
    decrypted = decrypt(encrypted, 3)
    print(secret)
    print(encrypted)
    print(decrypted)
