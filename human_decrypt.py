""" Demo: cracking code using a known ciphertext """
from substitution_cipher import decrypt

if __name__ == '__main__':
    plain_text = "MIJN PASSWORD MIJN VERANTWOORDING".lower()
    cipher_text = "DOPF HQLLVGKR DOPF CTKQFZVGGKROFU".lower()

    mapping = {}

    for i in range(len(plain_text)):
        mapping[cipher_text[i]] = plain_text[i]


    #print(mapping)

    print (decrypt(cipher_text, mapping))

