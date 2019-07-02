# Runtime: 436 ms, faster than 40.00% of Python3 online submissions for Word Ladder.
# Memory Usage: 14 MB, less than 67.86% of Python3 online submissions for Word Ladder.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        arr = set(wordList)
        deque = collections.deque([(beginWord, 1)])
        visited = set()
        alpha = string.ascii_lowercase
        while deque:
            word, length = deque.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for ch in alpha:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in arr and new_word not in visited:
                        deque.append((new_word, length + 1))
                        visited.add(new_word)
        return 0
