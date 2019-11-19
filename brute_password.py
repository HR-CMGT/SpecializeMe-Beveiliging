""" Demo: brute force finding a hash """
import hashlib

def create_password(password, alphabet, size):
    """ Recursive function to create permutations of a size, given an alphabet"""
    if len(password) == size:
        yield password
    else:
        for c in alphabet:
            for result in create_password(password + c, alphabet, size):
                yield result

if __name__ == '__main__':

    roel = "222489560036639a9e1e1e1440358ca7"
    emiel = "b8ec2eb5a93ecbf2b6fd6a46c1b5d100"
    bob = "009b74c5c394276786a66b998c02185a"
    bas = "b370c7fb08219b313b537e1c22d63ee7"
    rob = "2904dc629248221216a71d848caf39b7"

    hash_to_find = bob

    # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    for p in create_password("", list("abcdefghijklmnopqrstuvwxyz!"), 5):
        b = p.encode('utf-8')
        hash_object = hashlib.md5(b)
        if hash_object.hexdigest() == hash_to_find:
            print("FOUND")
            print(p)
