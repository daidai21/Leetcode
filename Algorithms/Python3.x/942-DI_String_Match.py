# Runtime: 80 ms, faster than 44.01% of Python3 online submissions for DI String Match.
# Memory Usage: 15 MB, less than 5.00% of Python3 online submissions for DI String Match.
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        A = []
        low, high = 0, len(S)
        for s in S:
            if s == 'I':
                A.append(low)
                low += 1
            else:
                A.append(high)
                high -= 1
        return A + [high]
