# Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = collections.Counter(arr)
        repeat_num = set()
        for k, v in dic.items():
            if v in repeat_num:
                return False
            else:
                repeat_num.add(v)
        return True
