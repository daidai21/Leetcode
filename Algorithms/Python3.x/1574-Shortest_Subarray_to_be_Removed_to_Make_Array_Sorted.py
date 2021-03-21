# 1574. Shortest Subarray to be Removed to Make Array Sorted


# Runtime: 604 ms, faster than 95.73% of Python3 online submissions for Shortest Subarray to be Removed to Make Array Sorted.
# Memory Usage: 28.9 MB, less than 45.60% of Python3 online submissions for Shortest Subarray to be Removed to Make Array Sorted.

# 删除以后最后剩下的元素必须是 Case:
#    1. 单独前缀
#    2. 单独后缀
#    3. 前缀加后缀


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r and arr[l] <= arr[l + 1]:
            l += 1
        if l == r:
            return 0  # arr is sorted
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        mv = min(len(arr) - l - 1, r)  # case 1, case 2
        # case 3: try to merge
        for l_i in range(l + 1):
            if arr[l_i] <= arr[r]:
                mv = min(mv, r - l_i - 1)
            elif r < len(arr) - 1:
                r += 1
            else:
                break
        return mv
