from string import ascii_lowercase


class Cipher(object):

    def __init__(self, key=None):
        self._key = key
        self.letter_map = ascii_lowercase[
            self.key:] + ascii_lowercase[:self.key]

    def encode(self, plaintext):
        return self._shift_letters(plaintext, ascii_lowercase, self.letter_map)

    def decode(self, ciphertext):
        return self._shift_letters(ciphertext, self.letter_map, ascii_lowercase)

    def _shift_letters(self, text, from_alpha, to_alpha):
        return_text = ''
        for index, char in enumerate(filter(str.isalpha, text)):
            map_index = from_alpha.index(char.lower())
            return_text += to_alpha[map_index]
        return return_text

    @property
    def key(self):
        return ascii_lowercase.index(self._key)


class Caesar(Cipher):

    def __init__(self):
        super(Caesar, self).__init__('d')
