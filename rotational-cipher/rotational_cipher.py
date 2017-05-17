import string

key = string.ascii_letters


def rotate(plain_text, shift_key):
    cipher_text = []
    for item in plain_text:
        i = (key.index(item) + shift_key) % 26
        cipher_text.append(key[i])
    return ''.join(cipher_text)
