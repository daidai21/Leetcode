# Runtime: 80 ms, faster than 18.38% of Python3 online submissions for Reveal Cards In Increasing Order.
# Memory Usage: 14 MB, less than 12.50% of Python3 online submissions for Reveal Cards In Increasing Order.
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = []
        for x in sorted(deck)[::-1]:
            d = [x] + d[-1:] + d[:-1]  # move max index to first, and append a the next biggest number to the left
        return d
