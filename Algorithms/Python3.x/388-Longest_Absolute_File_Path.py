# Runtime: 20 ms, faster than 99.03% of Python3 online submissions for Longest Absolute File Path.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Absolute File Path.
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1
        return max_len
