class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        if len_s == 1 or len_s == 0: return s
        start, end = 0, len_s - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
        return s
