# Time Limit Exceeded
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt_one = 0
        cnt_two = 0
        max_len = 0
        pre_sum_arr = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            pre_sum_arr[idx + 1] = pre_sum_arr[idx] + num
        for left in range(len(nums)):
            for right in range(left + 1, len(nums) + 1):
                if right - left == (pre_sum_arr[right] - pre_sum_arr[left]) * 2:
                    max_len = max(max_len, right - left)
        return max_len


# Runtime: 916 ms, faster than 78.11% of Python3 online submissions for Contiguous Array.
# Memory Usage: 18.3 MB, less than 65.64% of Python3 online submissions for Contiguous Array.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: -1}  # Key: count 0 1, Value: index
        max_len = 0
        cnt = 0
        for i in range(len(nums)):
            cnt += 1 if nums[i] == 1 else -1
            if cnt in dic:
                max_len = max(max_len, i - dic[cnt])
            else:
                dic[cnt] = i
        return max_len
