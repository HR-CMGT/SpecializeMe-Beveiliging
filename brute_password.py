import hashlib

def create_password(password, alphabet, size):
    if len(password) == size:
        yield password
    else:
        for c in alphabet:
            for result in create_password(password + c, alphabet, size):
                yield result


if __name__ == '__main__':

    pw = "hoi"
    b = pw.encode('utf-8')
    hash_object = hashlib.sha256(b)

    #hash_to_find = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08" # test

    hash_to_find = hash_object.hexdigest()

    for p in create_password("", list("abcdefghijklmnopqrstuvwxyz"), len(pw)):
        b = p.encode('utf-8')
        hash_object = hashlib.sha256(b)
        if hash_object.hexdigest() == hash_to_find:
            print("FOUND")
            print(p)


