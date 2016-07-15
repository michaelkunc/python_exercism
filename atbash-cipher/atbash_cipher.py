import string

GROUP_SIZE = 5
ENCODING = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])

def encode(plaintext):
    ciphertext = decode(plaintext)
    return ' '.join([ciphertext[i:i + GROUP_SIZE] for i in range(0, len(ciphertext), GROUP_SIZE)])

def decode(ciphertext):
	return ''.join(l for l in ciphertext.lower() if l.isalnum()).translate(ENCODING)

