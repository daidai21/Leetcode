# Runtime: 52 ms, faster than 84.18% of Python3 online submissions for Find Common Characters.
# Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions for Find Common Characters.
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        while len(A[0]) > 0:
            if all(A[0][0] in word for word in A[1:]):
                res.append(A[0][0])
                A = [word.replace(A[0][0], '', 1) for word in A]
            else:
                A[0] = A[0].replace(A[0][0], '', 1)
        return res
