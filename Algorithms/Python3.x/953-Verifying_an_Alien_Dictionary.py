# Runtime: 44 ms, faster than 62.33% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 13.6 MB, less than 16.67% of Python3 online submissions for Verifying an Alien Dictionary.
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: list(map(order.index, w)))
