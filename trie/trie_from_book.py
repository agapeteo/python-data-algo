### from book everyday algorithms book

ENDS_HERE = "#"

class Trie:
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def find(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return None
        return trie


some_trie = Trie()
some_trie.insert("alex")
some_trie.insert("alexander")
some_trie.insert("peter")

print(some_trie.find("alex"))
print(some_trie.find("peter"))
print(some_trie.find("vova"))
