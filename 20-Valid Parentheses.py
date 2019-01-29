class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                tmp = stack.pop() if stack else '?'
                if mapping[char] != tmp: return False  # 不对称
            else: stack.append(char)  # 压栈
        return not stack
