class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        self.__forward = ''.join(chr((k + shift) % 26 + ord('A')) for k in range(26))
        self.__backward = ''.join(chr((k - shift) % 26 + ord('A')) for k in range(26))

    def encrypt(self, message):
        """Return string representing encripted message."""
        return self.__transform(message, self.__forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self.__transform(secret, self.__backward)

    def __transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')                  # index from 0 to 25
                msg[k] = code[j]                            # replace this character
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)
