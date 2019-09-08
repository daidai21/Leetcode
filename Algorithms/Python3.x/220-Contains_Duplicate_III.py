# Runtime: 76 ms, faster than 31.87% of Python3 online submissions for Contains Duplicate III.
# Memory Usage: 16.1 MB, less than 33.33% of Python3 online submissions for Contains Duplicate III.
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0:
            return False
        dic = collections.OrderedDict()
        for n in nums:
            key = n if not t else n // t
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(m - n) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        return False
