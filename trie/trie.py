class Node:
    def __init__(self):
        self.nodes = {}
        self.is_last = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, text):
        cur_node = self.root
        idx = 0
        for char in text:
            try:
                next_node = cur_node.nodes[char]
            except KeyError:
                next_node = Node()
                cur_node.nodes[char] = next_node
            if idx == len(text) - 1:
                next_node.is_last = True
            cur_node = next_node
            idx += 1

    def __add__(self, other):
        self.add(other)

    def __contains__(self, text):
        cur_node = self.root
        idx = 0
        for char in text:
            try:
                next_node = cur_node.nodes[char]
            except KeyError:
                return False
            if idx == len(text) - 1 and next_node.is_last:
                return True
            cur_node = next_node
            idx += 1
        return False


def test():
    trie = Trie()
    trie.add("cat")
    trie.add("can")
    trie.add("cast")
    trie.add("boost")

    assert "cat" in trie
    assert "can" in trie
    assert "cast" in trie
    assert "boost" in trie

    assert "cas" not in trie
    assert "casting" not in trie
    assert "cost" not in trie
    assert "but" not in trie
    assert "bot" not in trie


if __name__ == "__main__":
    test()
