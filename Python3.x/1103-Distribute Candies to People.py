# Runtime: 60 ms, faster than 9.32% of Python3 online submissions for Distribute Candies to People.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Distribute Candies to People.
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        num, candies, idx = 1, candies - 1, 0
        while candies >= 0:
            res[idx % num_people] += num
            idx, num = idx + 1, num + 1
            if candies >= num:
                candies -= num
            else:
                break
        res[idx % num_people] += candies
        return res


# Runtime: 48 ms, faster than 30.04% of Python3 online submissions for Distribute Candies to People.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Distribute Candies to People.
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res, i = [0] * num_people, 0
        while candies > 0:
            res[i % num_people] += min(candies, i + 1)
            candies -= i + 1
            i += 1
        return res
