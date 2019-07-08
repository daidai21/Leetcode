# Runtime: 44 ms, faster than 86.89% of Python3 online submissions for Word Break II.
# Memory Usage: 13.3 MB, less than 70.68% of Python3 online submissions for Word Break II.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(s, wordDict, memo):
            if s in memo:
                return memo[s]
            if not s:
                return []
            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):
                    res.append(word)
                else:
                    tmp = helper(s[len(word):], wordDict, memo)
                    for item in tmp:
                        item = word + ' ' + item
                        res.append(item)
            memo[s] = res
            return res

        return helper(s, wordDict, {})
