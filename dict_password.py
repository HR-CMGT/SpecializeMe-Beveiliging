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

    pw = "tafelpoot"
    b = pw.encode('utf-8')
    hash_object = hashlib.sha256(b)

    # hash_to_find = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08" # test

    hash_to_find = hash_object.hexdigest()

    for wordlength in dictionary: #range(3, 10):  # excl max
        for word in dictionary[wordlength]:
            b = word.encode('utf-8')
            hash_object = hashlib.sha256(b)
            if hash_object.hexdigest() == hash_to_find:
                print("FOUND")
                print(word)