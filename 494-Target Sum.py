# hash
# Runtime: 228 ms, faster than 78.46% of Python3 online submissions for Target Sum.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Target Sum.
class Solution:
    def findTargetSumWays(self, nums: 'List[int]', S: 'int') -> 'int':
        dict = {0: 1}
        for item in nums:
            tmp_dict = {}
            for tmp_sum in dict:
                tmp_dict[tmp_sum + item] = tmp_dict.get(tmp_sum + item, 0) + dict[tmp_sum]
                tmp_dict[tmp_sum - item] = tmp_dict.get(tmp_sum - item, 0) + dict[tmp_sum]
            dict = tmp_dict
        return dict.get(S, 0)
