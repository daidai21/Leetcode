# mutiply pointer
# Runtime: 64 ms, faster than 89.44% of Python3 online submissions for String Compression.
# Memory Usage: 13.9 MB, less than 6.25% of Python3 online submissions for String Compression.
class Solution:
    def compress(self, chars: List[str]) -> int:
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                i += 1
                length += 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left += 1
            i += 1
        return left
