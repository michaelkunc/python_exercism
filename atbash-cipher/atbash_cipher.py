import string

DIGITS = ''.join(map(str, range(0,10)))
GROUP_SIZE = 5
PLAIN = string.ascii_lowercase
CIPHER = PLAIN[::-1]



def encode(plaintext):
    clean_plaintext = ''.join(l.lower() for l in plaintext if l.isalnum())
    ciphertext = clean_plaintext.translate(string.maketrans(PLAIN+DIGITS, CIPHER+DIGITS))
    return ' '.join([ciphertext[i:i+GROUP_SIZE] for i in range(0, len(ciphertext), GROUP_SIZE)])


def decode(ciphertext):
    return encode(ciphertext)
