# Runtime: 68 ms, faster than 42.24% of Python3 online submissions for Self Dividing Numbers.
# Memory Usage: 13.8 MB, less than 8.00% of Python3 online submissions for Self Dividing Numbers.
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            if self.is_self_divide_num(num):
                result.append(num)
        return result

    def is_self_divide_num(self, num):
        for n in str(num):
            if int(n) == 0:
                return False
            elif num % int(n) != 0:
                return False
        return True
