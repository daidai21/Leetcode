# Runtime: 136 ms, faster than 98.26% of Python3 online submissions for Add and Search Word - Data structure design.
# Memory Usage: 20.5 MB, less than 100.00% of Python3 online submissions for Add and Search Word - Data structure design.
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        elif '.' not in word:
            return word in self.word_dict[len(word)]
        else:
            for v in self.word_dict[len(word)]:
                for i, ch in enumerate(word):
                    if ch != v[i] and ch != '.':
                        break
                else:
                    return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
