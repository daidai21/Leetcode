# Runtime: 52 ms, faster than 44.43% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Bulls and Cows.
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        dic = {}
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                dic[s] = dic[s] + 1 if s in dic else 1
        for s, g in zip(secret, guess):
            if s != g and g in dic and dic[g] > 0:
                cows += 1
                dic[g] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'
