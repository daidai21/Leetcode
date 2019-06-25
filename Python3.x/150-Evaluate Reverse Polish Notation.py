# Runtime: 44 ms, faster than 79.43% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 13.1 MB, less than 93.61% of Python3 online submissions for Evaluate Reverse Polish Notation.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                num_2, num_1 = stack.pop(), stack.pop()
                if token == "+":
                    tmp = num_1 + num_2
                elif token == "-":
                    tmp = num_1 - num_2
                elif token == "*":
                    tmp = num_1 * num_2
                else:
                    tmp = num_1 / num_2
                stack.append(int(tmp))
        return stack[0]
