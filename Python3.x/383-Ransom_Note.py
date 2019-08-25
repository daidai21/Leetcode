# Runtime: 76 ms, faster than 29.18% of Python3 online submissions for Ransom Note.
# Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Ransom Note.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine, ransomNote = list(magazine), list(ransomNote)
        for j, r in enumerate(ransomNote):
            if r in magazine:
                magazine[magazine.index(r)] = None
            else:
                return False
        return True
