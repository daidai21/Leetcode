# Runtime: 32 ms, faster than 72.65% of Python3 online submissions for Reverse Only Letters.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Only Letters.
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left, right = 0, len(S) - 1
        S = list(S)
        while left < right:
            while left < right and not S[left].isalpha():
                left += 1
            while left < right and not S[right].isalpha():
                right -= 1
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
        return ''.join(S)
