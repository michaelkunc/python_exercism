from string import ascii_lowercase


class Cipher(object):

    def __init__(self, key=None):
        self._key = key

    def encode(self, plaintext):
        cipher_text = ''
        key_list = self.key * (int(len(plaintext) / len(self.key)) + 1)
        for index, char in enumerate(filter(str.isalpha, plaintext.lower())):
            i = (ascii_lowercase.index(char) + key_list[index]) % 26
            cipher_text += ascii_lowercase[i]
        return cipher_text

    def decode(self, ciphertext):
        plaintext = ''
        key_list = self.key * (int(len(ciphertext) / len(self.key)) + 1)
        for index, char in enumerate(filter(str.isalpha, ciphertext.lower())):
            i = (ascii_lowercase.index(char) - key_list[index]) % 26
            plaintext += ascii_lowercase[i]
        return plaintext

    # @staticmethod
    # def _shift_letters(text, from_alpha, to_alpha):
    #     return_text = ''
    #     for index, char in enumerate(filter(str.isalpha, text)):
    #         map_index = from_alpha.index(char.lower())
    #         return_text += to_alpha[map_index]
    #     return return_text

    @property
    def key(self):
        return [ascii_lowercase.index(item) for item in self._key]


class Caesar(Cipher):

    def __init__(self):
        super(Caesar, self).__init__('d')
