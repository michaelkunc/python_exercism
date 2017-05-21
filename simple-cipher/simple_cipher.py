import string


class Cipher(object):

    ALPHABET = string.ascii_lowercase

    def __init__(self, key=None):
        self._key = key
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
        return string.ascii_lowercase.index(self._key)


class Caesar(Cipher):

    def __init__(self):
        super(Caesar, self).__init__('d')

    # ALPHABET = string.ascii_lowercase

    # def __init__(self, key=None):
    #     if not key:
    #         self.key = 3
    #     else:
    #         self.key = key
    #     self.letter_map = Caesar.ALPHABET[
    #         self.key:] + Caesar.ALPHABET[:self.key]

    # def encode(self, plaintext):
    #     ciphertext = ''
    #     for index, char in enumerate(filter(str.isalpha, plaintext)):
    #         map_index = Caesar.ALPHABET.index(char.lower())
    #         ciphertext += self.letter_map[map_index]
    #     return ciphertext

    # def decode(self, ciphertext):
    #     plaintext = ''
    #     for index, char in enumerate(filter(str.isalpha, ciphertext)):
    #         map_index = self.letter_map.index(char.lower())
    #         plaintext += Caesar.ALPHABET[map_index]
    #     return plaintext
