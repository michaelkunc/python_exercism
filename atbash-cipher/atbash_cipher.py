import string

GROUP_SIZE = 5
PLAIN = string.ascii_lowercase
CIPHER = PLAIN[::-1]
ENCODING = string.maketrans(PLAIN, CIPHER)

def encode(plaintext):
    ciphertext = encode_decode(clean_text(plaintext))
    return ' '.join([ciphertext[i:i + GROUP_SIZE] for i in range(0, len(ciphertext), GROUP_SIZE)])


def decode(ciphertext):
    return encode_decode(clean_text(ciphertext))


def clean_text(text):
    return ''.join(l.lower() for l in text if l.isalnum())


def encode_decode(text):
    return text.translate(ENCODING)
