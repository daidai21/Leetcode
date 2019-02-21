# stack
class Solution(object):
    def decodeString(self, s):
        stack, num, string = [], 0, ''
        for char in s:
            if char == '[':  # 开始，进栈
                stack.append(string)
                stack.append(num)
                string, num = '', 0
            elif char == ']':  # 结束，出栈
                num = stack.pop()
                pre_string = stack.pop()
                string = pre_string + num * string
                num = 0
            elif char.isdigit():  # 是数字
                num = num * 10 + int(char)
            else:  # 字符串
                string += char
            print(string, stack, num)
        return string
