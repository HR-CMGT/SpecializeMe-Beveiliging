""" Demo: finding a hash using a dictionary """
import hashlib

if __name__ == '__main__':
    dictionary = {}

    files = ['OpenTaal-210G-basis-gekeurd.txt', 'OpenTaal-210G-basis-ongekeurd.txt', 'OpenTaal-210G-flexievormen.txt']
    i = 0
    for fn in files:
        f = open(fn)
        line = f.readline()

        while line:
            i += 1
            word = line.rstrip()
            if len(word) not in dictionary:
                dictionary[len(word)] = []
            dictionary[len(word)].append(word)
            line = f.readline()
        f.close()

    print(i, "words loaded into dictionary")

    roel = "222489560036639a9e1e1e1440358ca7"
    emiel = "b8ec2eb5a93ecbf2b6fd6a46c1b5d100"
    bob = "009b74c5c394276786a66b998c02185a"
    bas = "b370c7fb08219b313b537e1c22d63ee7"
    rob = "2904dc629248221216a71d848caf39b7"


    hash_to_find = emiel

    for wordlength in dictionary: # can be optimized if you know the length
        for word in dictionary[wordlength]:
            b = word.encode('utf-8')
            hash_object = hashlib.md5(b)

            if hash_object.hexdigest() == hash_to_find:
                print("FOUND")
                print(word)