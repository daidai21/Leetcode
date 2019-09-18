# Runtime: 36 ms, faster than 82.69% of Python3 online submissions for Maximum Number of Balloons.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons.
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {
            'b': 0,  # 1
            'a': 0,  # 1
            'l': 0,  # 2
            'o': 0,  # 2
            'n': 0,  # 1
        }
        for ch in text:
            if ch in dic:
                dic[ch] += 1
        return min(dic['b'], dic['a'], dic['l'] // 2, dic['o'] // 2, dic['n'])
