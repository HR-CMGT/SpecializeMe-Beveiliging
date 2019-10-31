class Try():
    def __init__(self):
        self.root = {}
        self.next = self.root

    def addWord(self, word):
        next = self.root
        node = None

        for c in list(word.lower()):
            #print(c)
            if c not in next:
                next[c] = TryNode(c)
            node = next[c]
            next = node.next

        node.isWord = True

    def checkSpelling(self, word):
        next = self.root
        node = None
        for c in list(word):
            if c not in next:
                return False
            else:
                node = next[c]
                next = node.next
        return node.isWord


class TryNode():
    def __init__(self, c):
        self.c = c
        self.isWord = False
        self.next = {}

root_try = None

def decrypt(cipher_text, mapping):
    plain_text = list(cipher_text)
    for i in range(len(plain_text)):
        if cipher_text[i] in mapping:
            plain_text[i] = mapping[cipher_text[i]]
        else:
            plain_text[i] = '-'
    return "".join(plain_text)

def crack_code(cipher_text, mapping, cipher_position, try_node):

    # cipher end
    if cipher_position == len(cipher_text):
        print(decrypt(cipher_text, mapping))
        #print(mapping)
        return False # force to check all possibilities
    # word end
    if cipher_text[cipher_position] == " ":
        if try_node.isWord:
            return crack_code(cipher_text, mapping, cipher_position + 1, root_try)
        else:
            return False
    # existing char
    if cipher_text[cipher_position] in mapping:
        if mapping[cipher_text[cipher_position]] in try_node.next:
            return crack_code(cipher_text, mapping, cipher_position + 1, try_node.next[mapping[cipher_text[cipher_position]]])
        else:
            return False
    # new char
    else:
        for (c, t) in try_node.next.items():
            # skip if char already in cipher
            if c not in mapping.values():
                mapping_new = mapping.copy()
                mapping_new[cipher_text[cipher_position]] = c
                if crack_code(cipher_text, mapping_new, cipher_position + 1, try_node.next[c]):
                    return True

        return False

if __name__ == '__main__':
    root_try = Try()

    files = ['OpenTaal-210G-basis-gekeurd.txt', 'OpenTaal-210G-basis-ongekeurd.txt', 'OpenTaal-210G-flexievormen.txt']
    i = 0
    for fn in files:
        f = open(fn)
        line = f.readline()

        while line:
            i += 1
            root_try.addWord(line.rstrip())
            line = f.readline()
        f.close()

    #print("test: ", root_try.checkSpelling("bewaar"))

    #exit()

    print(i, "words loaded into try")

    cipher_text = "DOPF HQLLVGKR DOPF CTKQFZVGGKROFU"

    #cipher_text = "wrg rh vvm tvsvrnv yllwhxszk svg rh svvo yvozmtirqp wzg mrvnzmw pzm zxsgviszovm dzg srvi hgzzg wzziln tvyifrpvm dv vvm tvsvrnv xlwv"

    crack_code(cipher_text.lower(), {}, 0, root_try)
