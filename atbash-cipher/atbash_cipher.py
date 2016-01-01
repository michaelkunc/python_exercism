import string

DIGITS = ''.join(map(str, range(0, 10)))
GROUP_SIZE = 5
PLAIN = string.ascii_lowercase
CIPHER = PLAIN[::-1]


def encode(plaintext):
    ciphertext = encode_decode(clean_text(plaintext), PLAIN, CIPHER)
    return ' '.join([ciphertext[i:i + GROUP_SIZE] for i in range(0, len(ciphertext), GROUP_SIZE)])


def decode(ciphertext):
    return encode_decode(clean_text(ciphertext), CIPHER, PLAIN)


def clean_text(text):
    return ''.join(l.lower() for l in text if l.isalnum())


def encode_decode(text, plain, cipher):
    return text.translate(string.maketrans(plain, cipher))
