"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def search(self, word):
        node = self.search_prefix(word)

        # If word is found, only return `True` if end of trie matches end of searched
        # word to ensure whole word match is found
        return node and node.is_end

    def starts_with(self, prefix):
        node = self.search_prefix(prefix)
        return bool(node)

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            else:
                node = node.children[char]
        return node


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    ans_1 = trie.search("apple")  # return True
    ans_2 = trie.search("app")  # return False
    ans_3 = trie.starts_with("app")  # return True
    trie.insert("app")
    ans_4 = trie.search("app")  # return True
    print(ans_1, ans_2, ans_3, ans_4)
