# Runtime: 44 ms, faster than 51.70% of Python3 online submissions for Different Ways to Add Parentheses.
# Memory Usage: 13.8 MB, less than 11.11% of Python3 online submissions for Different Ways to Add Parentheses.
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        if len(input) == 0:
            return res
        elif '+' not in input and '-' not in input and '*' not in input:
            return [int(input)]
        for idx, val in enumerate(input):
            if val in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:idx])
                right = self.diffWaysToCompute(input[idx + 1:])
                for l in left:
                    for r in right:
                        if val == '+':
                            res.append(int(l) + int(r))
                        elif val == '-':
                            res.append(int(l) - int(r))
                        elif val == '*':
                            res.append(int(l) * int(r))
        return res
