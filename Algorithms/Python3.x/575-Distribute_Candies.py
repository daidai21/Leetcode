from typing import List


# Runtime: 1288 ms, faster than 6.76% of Python3 online submissions for Distribute Candies.
# Memory Usage: 14.8 MB, less than 25.00% of Python3 online submissions for Distribute Candies.
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        mem = [False] * 10005
        for candy in candies:
            mem[candy] = True
        diff_candy_num = sum(mem)
        return min(len(candies) // 2, diff_candy_num)


if __name__ == "__main__":
    print(Solution().distributeCandies([1,1,2,2,3,3]))  # 3
    print(Solution().distributeCandies([1,1,2,3]))  # 2
