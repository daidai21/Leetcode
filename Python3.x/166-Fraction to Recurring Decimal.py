# Runtime: 32 ms, faster than 92.40% of Python3 online submissions for Fraction to Recurring Decimal.
# Memory Usage: 13.3 MB, less than 19.36% of Python3 online submissions for Fraction to Recurring Decimal.
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        if denominator == 0:
            return "" 
        if (numerator > 0 and denominator > 0) or (numerator < 0 and denominator < 0):
            res = ""
        else:
            res = "-"
            numerator, denominator = abs(numerator), abs(denominator)
        if numerator % denominator == 0:
            res += str(int(numerator / denominator))
        else:
            res += str(int(numerator / denominator)) + '.'
            remain = numerator % denominator  # 余数
            idx = len(res)
            remain_dict = {}
            while remain and remain not in remain_dict:
                remain_dict[remain] = idx
                idx += 1
                remain *= 10
                res += str(int(remain / denominator))
                remain %= denominator
            if remain:  # 是否是循环
                res = res[:remain_dict[remain]] + '(' + res[remain_dict[remain]:]
                res += ')'
        return res
