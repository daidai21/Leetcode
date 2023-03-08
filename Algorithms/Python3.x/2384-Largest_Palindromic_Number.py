# https://leetcode.com/problems/largest-palindromic-number/
# 2384. 最大回文数字



class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        nm = [0] * 10
        for s in num:
            nm[int(s)] += 1
        print(nm)

        # 全是0的情况
        if nm[0] == sum(nm):
            return "0"

        # 填左边的
        left = ""
        for i in range(9, 0, -1):
            left += str(i) * (nm[i] // 2)
        
        
        # 左边有值 可以填0
        if len(left) >= 1:
            left += '0' * (nm[0] // 2)

        # 奇数个的情况
        mid = ""
        for i in range(9, -1, -1):
            if nm[i] % 2 == 1:
                mid = str(i)
                break
        
        return left + mid + left[::-1]
