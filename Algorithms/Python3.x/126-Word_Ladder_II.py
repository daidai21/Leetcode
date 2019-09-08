# Runtime: 520 ms, faster than 37.80% of Python3 online submissions for Word Ladder II.
# Memory Usage: 16.7 MB, less than 16.67% of Python3 online submissions for Word Ladder II.
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        result = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        while layer:
            new_layer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    result.extend(k for k in layer[word])
                else:
                    for i in range(len(word)):
                        for ch in "abcdefghijklmnopqrstuvwxyz":
                            new_word = word[:i] + ch + word[i + 1:]
                            if new_word in wordList:
                                new_layer[new_word] += [w + [new_word] for w in layer[word]]
            wordList -= set(new_layer.keys())
            layer = new_layer
        return result
