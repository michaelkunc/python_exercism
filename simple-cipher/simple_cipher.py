import string


class Cipher(object):

    def __init__(self, key):
        self.key = key

    def encode(self, plaintext):
        c = Caesar()
        return c.encode(plaintext)


class Caesar(object):
    ALPHABET = string.ascii_lowercase

    def __init__(self):
        self.letter_map = Caesar.ALPHABET[
            self.key:] + Caesar.ALPHABET[:self.key]

    def encode(self, plaintext):
        ciphertext = ''
        for index, char in enumerate(filter(str.isalpha, plaintext)):
            map_index = Caesar.ALPHABET.index(char.lower())
            ciphertext += self.letter_map[map_index]
        return ciphertext

    def decode(self, ciphertext):
        plaintext = ''
        for index, char in enumerate(filter(str.isalpha, ciphertext)):
            map_index = self.letter_map.index(char.lower())
            plaintext += Caesar.ALPHABET[map_index]
        return plaintext

    @property
    def key(self):
        return 3

    @key.setter
    def key(self, key):
        return Caesar.ALPHABET.index(key)
