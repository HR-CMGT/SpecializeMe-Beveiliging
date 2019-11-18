""" Demo: cracking code using a known ciphertext """
from substitution_cipher import decrypt

if __name__ == '__main__':
    plain_text = "MIJN PASSWORD MIJN VERANTWOORDING".lower()
    cipher_text = "DOPF HQLLVGKR DOPF CTKQFZVGGKROFU".lower()

    secret_text = "iqeatf wsopyz cggkwtigxrtf qqf lsoddtkoatf"#"iqeatf ol aofrtklhts"

    mapping = {}

    for i in range(len(plain_text)):
        mapping[cipher_text[i]] = plain_text[i]


    #print(mapping)

    print (decrypt(secret_text, mapping))

