# 
class Solution:
    def numDupDigitsAtMostN(self, N):
        def func(n):
            if n == 0 or n == 1:
                return 1
            return func(n - 1) * n

        def pick(m, n):  # 从 n 中挑出 m ，范围问题
            return func(n) // func(n - m)

        nums = [int(d) for d in str(N + 1)]  # N + 1 作为填充
        K = len(nums)  # N 有 K 个数
        cnt = 0  # 数字没有重复值
        for i in range(1, K):  # 数小于 K 的正数
            cnt += 9 * pick(i - 1, 9)
        seen = set()  # 用 K 位数计数
        for i in range(K):
            # 前缀 = nums[:i] + 当前数字
            # 当前数字 < nums[i]
            for x in range(1 if i == 0 else 0, nums[i]):
                if x in seen:  # 避免重复
                    continue
                cnt += pick(K - (i + 1), 10 - (i + 1))
            if nums[i] in seen:  # 从下一次迭代开始，前缀有重复的数字，break
                break
            seen.add(nums[i])
        return N - cnt


'''
计算res为 N - total 没有重复数字。
变成了一个数学和排列问题。

从 m 中选 n
P(m, n): n! / (n-m)!

算法：
    1） 假设 N 有 k 个数字
        假设数字是 i
        第一个数字 1 ~ 9，后面的选项是 0 ~ 9 没有第一个数字
        count = 9 * P(i-1,9)
    2） count 数字有 k 位
        计算前缀相同的数字
        前缀不能有相同数字
        对于 77xx 这样的情况，我们应当停止计算
'''


class Solution:
    def numDupDigitsAtMostN(self, N):
        def func(n):
            return 1 if n == 0 or n == 1 else func(n - 1) * n

        def pick(m, n): return func(n) // func(n - m)

        nums = [int(d) for d in str(N + 1)]
        K, cnt = len(nums), 0
        for i in range(1, K): cnt += 9 * pick(i - 1, 9)
        seen = set()  # 用 K 位数计数
        for i in range(K):
            for x in range(1 if i == 0 else 0, nums[i]):
                if x in seen: continue
                cnt += pick(K - (i + 1), 10 - (i + 1))
            if nums[i] in seen: break
            seen.add(nums[i])
        return N - cnt
