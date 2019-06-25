# Runtime: 80 ms, faster than 97.46% of Python3 online submissions for Basic Calculator II.
# Memory Usage: 15.2 MB, less than 23.09% of Python3 online submissions for Basic Calculator II.
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "") + "+"
        stack, num, sign = [], 0, "+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                continue
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(int(stack.pop() / num))
            num, sign = 0, c
        return sum(stack)
