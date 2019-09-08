class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = [0] * 61
        for t in time:
            mod[-1] += mod[(60 - t % 60) % 60]  # mod[60]存储的是结果
            mod[t % 60] += 1  # mod[0 ~ 59]存储的是[0 ~ 59]在time数组中的次数
        return mod[-1]


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = collections.Counter()
        result = 0
        for t in time:
            result += count[-t % 60]
            count[t % 60] += 1
        return result


'''
Calculate the time % 60 then it will be exactly same as two sum problem.
t % 60 gets the remainder 0 ~ 59.
We count the occurrence of each remainders in a array/hashmap c.
we want to know that, for each t, how many x satisfy (t + x) % 60 = 0.
t % 60 + x % 60 = 60 for the most cases.
It has to be noticed that, if t % 60 = 0, x % 60 = 0 instead of 60.
60 - t % 60 will get a number in range 1 ~ 60.
(60 - t % 60) % 60 can get number in range 0 ~ 59
'''
