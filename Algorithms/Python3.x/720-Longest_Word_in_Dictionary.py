# Runtime: 68 ms, faster than 97.13% of Python3 online submissions for Longest Word in Dictionary.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Word in Dictionary.
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words_set, longest_word = set([""]), ""
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word
