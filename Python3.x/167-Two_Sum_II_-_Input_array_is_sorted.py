# Runtime: 76 ms, faster than 60.22% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.3 MB, less than 5.80% of Python3 online submissions for Two Sum II - Input array is sorted.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1, i2 = 0, len(numbers) - 1
        while numbers[i1] + numbers[i2] != target:
            if numbers[i1] + numbers[i2] > target:
                i2 -= 1
            else:
                i1 += 1
        return [i1 + 1, i2 + 1]
