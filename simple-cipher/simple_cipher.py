from string import ascii_lowercase
import random


class Cipher(object):

    def __init__(self, key=None):
        self._key = key

    def encode(self, plain):
        return self._shift_letters(plain, self._shift_length(plain))

    def decode(self, cipher):
        negative_offset = [i * -1 for i in self._shift_length(cipher)]
        return self._shift_letters(cipher, negative_offset)

    def _shift_length(self, text):
        return [ascii_lowercase.index(item) for item in self.key] * (int(len(text) / len(self.key)) + 1)

    @staticmethod
    def _shift_letters(text, shift_length):
        return_text = ''
        for index, char in enumerate(filter(str.isalpha, text.lower())):
            i = (ascii_lowercase.index(char) +
                 shift_length[index]) % 26
            return_text += ascii_lowercase[i]
        return return_text

    @property
    def key(self):
        if not self._key:
            return ''.join([random.choice(ascii_lowercase) for i in range(100)])
        else:
            return self._key


class Caesar(Cipher):

    def __init__(self):
        super(Caesar, self).__init__('d')
