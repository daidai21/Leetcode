# Runtime: 64 ms, faster than 84.40% of Python3 online submissions for Repeated DNA Sequences.
# Memory Usage: 25.5 MB, less than 66.67% of Python3 online submissions for Repeated DNA Sequences.
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = set()
        res = set()        
        for i in range(len(s) - 9):
            cur = s[i:i + 10]
            if cur in sequences:
                res.add(cur)
            else:
                sequences.add(cur)
        return list(res)
