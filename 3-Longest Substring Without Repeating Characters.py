class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, start, char_dict = 0, 0, {}
        for i, char in enumerate(s, start=1):  # enumerate这里的start是从1开始循环，而不是0
            if char_dict.get(char, -1) >= start:  # 这里的dict.get(char, -1)中的-1的意思是当没有得到的时候返回-1
                start = char_dict[char]
            char_dict[char] = i  # 向map容器中添加key：字符char；value：i下标
            max_len = max(max_len, i - start)
        return max_len


'''
用2个变量（start, end）分别保存子串的起点和终点。
end自增，直到遇到重复字符为止；
从重复字符出现的位置之后1位重新开始扫描。
'''