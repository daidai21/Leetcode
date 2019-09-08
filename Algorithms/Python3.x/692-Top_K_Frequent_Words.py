# Runtime: 60 ms, faster than 93.04% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 13.6 MB, less than 8.33% of Python3 online submissions for Top K Frequent Words.
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        candidates = list(count.keys())
        candidates.sort(key=lambda w: (-count[w], w))
        return candidates[:k]
