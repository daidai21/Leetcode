# Runtime: 24 ms, faster than 99.90% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.9 MB, less than 44.78% of Python3 online submissions for Kids With the Greatest Number of Candies.
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_candies = max(candies)
        for i in candies:
            res.append(i + extraCandies >= max_candies)
        return res
