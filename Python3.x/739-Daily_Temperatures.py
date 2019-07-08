# 暴力
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        res = [0 for _ in range(length)]
        for i in range(length):
            j = i
            for k in range(i + 1, length):
                if T[k] > T[i]:
                    j = k
                    break
            res[i] = j - i
        return res


# 向前迭代的栈
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in T]
        stack = []  # 存储到当前节点之前还没找到res的索引值
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:  # 
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res
