class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = score = 0
        seen = {}
        for idx, hour in enumerate(hours):
            score = score + 1 if hour > 8 else score - 1
            if score > 0:
                res = idx + 1
            seen.setdefault(score, idx)
            if score - 1 in seen:
                res = max(res, idx - seen[score - 1])
        return res
