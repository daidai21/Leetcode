# 回溯
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_ = []

        def backstrack(tmp='', left=0, right=0):  # 回溯
            if len(tmp) == 2 * n:  # 中止条件
                list_.append(tmp)
                return
            if left < n: backstrack(tmp + '(', left + 1, right)  # 
            if right < left: backstrack(tmp + ')', left, right + 1)

        backstrack()
        return list_
