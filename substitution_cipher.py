def decrypt(cipher_text, mapping):
    """ Decrypt substitute cipher using a mapping """
    plain_text = list(cipher_text)
    for i in range(len(plain_text)):
        if cipher_text[i] in mapping:
            plain_text[i] = mapping[cipher_text[i]]
        else:
            plain_text[i] = '-'
    return "".join(plain_text)