# sorted
# Runtime: 72 ms, faster than 47.08% of Python3 online submissions for Valid Anagram.
# Memory Usage: 13.3 MB, less than 0.96% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        return sorted(s) == sorted(t)


# 暴力
# time: 5076 ms, faster than 0.99%
# space: 12.4 MB, less than 0.96%
class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        if len(s) != len(t): return False
        for letter in t:
            if t.count(letter) != s.count(letter): return False
        return True

# 暴力的优化
# time: 36 ms, faster than 99.98%
# space: 12.7 MB, less than 0.96%
class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        if len(s) != len(t): return False
        visited = set()
        for letter in t:
            if letter not in visited:
                visited.add(letter)
                if t.count(letter) != s.count(letter):
                    return False
        return True
