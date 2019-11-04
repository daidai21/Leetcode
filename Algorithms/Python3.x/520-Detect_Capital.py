# Runtime: 40 ms, faster than 41.98% of Python3 online submissions for Detect Capital.
# Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Detect Capital.
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        elif word[0].islower():
            return all([ch.islower() for ch in word[1:]])
        else:  # word[0].isupper()
            return len(set(ch.islower() for ch in word[1:])) == 1


# Runtime: 52 ms, faster than 5.32% of Python3 online submissions for Detect Capital.
# Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Detect Capital.
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


# Runtime: 40 ms, faster than 41.98% of Python3 online submissions for Detect Capital.
# Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Detect Capital.
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word[1:] == word[1:].lower() or word == word.upper()
