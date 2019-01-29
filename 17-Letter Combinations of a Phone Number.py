# 递归算法
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        phone = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        tmp_list = ['']
        for i in map(int, list(digits)):
            tmp = []
            for j in tmp_list:
                for k in phone[i]:
                    tmp.append(j + k)
            tmp_list = tmp
        return tmp_list
