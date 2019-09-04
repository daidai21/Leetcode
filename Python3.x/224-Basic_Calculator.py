# Runtime: 80 ms, faster than 95.68% of Python3 online submissions for Basic Calculator.
# Memory Usage: 15.3 MB, less than 7.14% of Python3 online submissions for Basic Calculator.
class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        stack = []
        num = 0
        sign = 1  # 1 is +, -1 is -
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                result += sign * num
                sign = 1
                num = 0
            elif c == '-':
                result += sign * num
                sign = -1
                num = 0
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ')':
                result += sign * num
                result *= stack.pop()
                result += stack.pop()
                num = 0
            else:
                continue
        return result + sign * num
