# dfs
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.tmp = []
        candidates.sort()
        self.dfs(candidates, [], target, 0)
        return self.tmp

    def dfs(self, candidates, tmp_list, target, n):
        if target == 0: self.tmp.append(tmp_list[:])
        if target < candidates[0]: return
        for i in candidates:
            if i > target: return
            if i < n: continue
            tmp_list.append(i)  # 栈
            self.dfs(candidates, tmp_list, target - i, i)
            tmp_list.pop()


'''
# 递归
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        output, length = [], len(candidates)
        def func(tmp, candidates, target, n):
            if sum(tmp) > target: return
            if sum(tmp) == target: return output.append(tmp)
            for i in range(n, length):
                func(tmp + [candidates[i]], candidates, target, i)

        func([], candidates, target, 0)
        return output
'''
