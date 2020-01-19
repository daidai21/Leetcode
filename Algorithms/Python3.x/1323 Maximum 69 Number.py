class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for idx, val in enumerate(num):
            if val == '6':
                num[idx] = '9'
                break
        return int("".join(num))


print(Solution().maximum69Number(9669))
print(Solution().maximum69Number(9996))
print(Solution().maximum69Number(9999))
