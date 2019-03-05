# 字典前缀树
class TrieNode:
    # Initialize data structure
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # param {string} word
        # return {void}
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # param {string} word
        # return {boolean}
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # param {string} prefix
        # return {boolean}
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
