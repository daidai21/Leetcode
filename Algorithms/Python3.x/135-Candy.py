# Runtime: 184 ms, faster than 75.36% of Python3 online submissions for Candy.
# Memory Usage: 16.3 MB, less than 40.00% of Python3 online submissions for Candy.
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candys = [1] * len(ratings)
        # left -> right
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candys[i] = candys[i - 1] + 1
        # right -> left
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candys[i] = max(candys[i], candys[i + 1] + 1)
        return sum(candys)
