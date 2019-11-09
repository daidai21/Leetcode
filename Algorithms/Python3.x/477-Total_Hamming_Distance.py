# Time Limit Exceeded
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        distance = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                distance += self.bit_count_one(nums[i] ^ nums[j]);
        return distance

    def bit_count_one(self, num):
        cnt = 0
        while num > 0:
            cnt += num & 1
            num >>= 1
        return cnt


# Runtime: 944 ms, faster than 6.81% of Python3 online submissions for Total Hamming Distance.
# Memory Usage: 14.2 MB, less than 83.33% of Python3 online submissions for Total Hamming Distance.
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bits = [[0, 0] for _ in range(32)]
        for num in nums:
            for i in range(32):
                bits[i][num % 2] += 1
                num = int(num / 2)
        return sum(n0 * n1 for n0, n1 in bits)
