# Runtime: 28 ms, faster than 73.40% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            tmp1 = max(stones)  # the first heaviest
            stones.pop(stones.index(tmp1))
            tmp2 = max(stones)  # the second heaviest
            stones.pop(stones.index(tmp2))
            if tmp1 != tmp2:
                stones.append(tmp1 - tmp2)
        return stones[0] if stones else 0
