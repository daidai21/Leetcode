from typing import List

# Time Limit Exceeded
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    temp = words[i] + words[j]
                    if temp == temp[::-1]:
                        pairs.append([i, j])
        return pairs


# Runtime: 464 ms, faster than 86.90% of Python3 online submissions for Palindrome Pairs.
# Memory Usage: 14.9 MB, less than 7.14% of Python3 online submissions for Palindrome Pairs.
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words = {word: i for i, word in enumerate(words)}
        pairs = []
        for word, i in words.items():
            len_word = len(word)
            for j in range(len_word + 1):
                left, right = word[:j], word[j:]
                if left == left[::-1]:
                    back = right[::-1]
                    if back != word and back in words:
                        pairs.append([words[back], i])
                if j != len_word and right == right[::-1]:
                    back = left[::-1]
                    if back != word and back in words:
                        pairs.append([i, words[back]])
        return pairs
