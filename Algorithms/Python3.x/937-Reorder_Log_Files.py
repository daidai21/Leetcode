# Runtime: 48 ms, faster than 29.94% of Python3 online submissions for Reorder Log Files.
# Memory Usage: 13.7 MB, less than 7.69% of Python3 online submissions for Reorder Log Files.
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = list(filter(lambda x: x.split()[1].isalpha(), logs))
        digits = list(filter(lambda x: x.split()[1].isdigit(), logs))
        letters.sort(key=lambda x: x.split()[0])
        letters.sort(key=lambda x: x.split()[1:])
        return letters + digits
