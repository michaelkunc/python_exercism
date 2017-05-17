import string

key = string.ascii_lowercase


def rotate(plain_text, shift_key):
    cipher_text = []
    for item in plain_text:
        try:
            i = (key.index(item.lower()) + shift_key) % 26
            if item.isupper():
                cipher_text.append(key[i].upper())
            else:
                cipher_text.append(key[i])
        except ValueError:
            cipher_text.append(item)
    return ''.join(cipher_text)
