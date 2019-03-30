# Runtime: 116 ms, faster than 26.14% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.7 MB, less than 5.12% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_multiply = 1
        have_zero = 0
        for num in nums:
            if num != 0:
                all_multiply *= num
            else:
                have_zero += 1

        if have_zero == 0:
            return [int(all_multiply / num) for num in nums]
        if have_zero == 1:
            return [0 if num else all_multiply for num in nums]
        if have_zero > 1:
            return [0 for _ in nums]


'''
首先计算所有和 & 计算列中有多少个0
分为三个情况：
    有0个0：
        常规操作  all_multiply / num
    有1个0
        是0的那项为 all_multiply，其余项为  all_multiply / num
    有超过1个0
        所有项为0
'''


# optimize
# Runtime: 96 ms, faster than 82.00% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.7 MB, less than 5.12% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiply, zero = 1, 0
        for num in nums:
            if num: multiply *= num
            else: zero += 1
        if zero == 0: return [int(multiply / num) for num in nums]
        if zero == 1: return [0 if num else multiply for num in nums]
        if zero > 1: return [0 for _ in nums]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        multiply = 1
        result = []
        for num in nums:
            result.append(multiply)
            multiply *= num
        multiply = 1
        for i in range(length - 1, -1, -1):
            result[i] = result[i] * multiply
            multiply *= nums[i]
        return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length, multiply, result = len(nums), 1, []
        for num in nums:
            result.append(multiply)
            multiply *= num
        multiply = 1
        for i in range(length - 1, -1, -1): result[i], multiply = result[i] * multiply, multiply * nums[i]
        return result
