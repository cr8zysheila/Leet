# Case sensitive Trie
class Trie(object):

    def __init__(self):
        self.trie_root = {}



    def insert(self, word):
        if not self.search(word):
            curr = self.trie_root
            for l in word:
                if l not in curr:
                    curr[l] = {}
                curr = curr[l]

            # mark the end of the word
            curr['*'] = {}


    def search(self, word):
        curr = self.prefixEnd(word)
        if not curr:
            return False

        # if curr is None, it'll cause 
        #TypeError: argument of type 'NoneType' is not iterable
        return '*' in curr


    def startsWith(self, prefix):
        curr = self.prefixEnd(prefix)
        return True if curr else False

    def prefixEnd(self, word):
        curr = self.trie_root
        for l in word:
            if l not in curr:
                return None

            curr = curr[l]

        return curr

test_trie = Trie()
test_trie.insert("fabulous")
print "after insert", test_trie.trie_root
print test_trie.search("fabulous")

print test_trie.search('fab')
print test_trie.search('b')
print test_trie.startsWith("fab")
print test_trie.startsWith('b')

