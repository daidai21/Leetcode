# Time Limit Exceeded
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        res = []
        for a in range(len_nums - 3):
            for b in range(a + 1, len_nums - 2):
                for c in range(b + 1, len_nums - 1):
                    for d in range(c + 1, len_nums):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target and [nums[a], nums[b], nums[c], nums[d]] not in res:
                            res.append([nums[a], nums[b], nums[c], nums[d]])
        return res


# space change time
# Runtime: 128 ms, faster than 77.10% of Python3 online submissions for 4Sum.
# Memory Usage: 17.4 MB, less than 8.74% of Python3 online submissions for 4Sum.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dic = dict()
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                sum_2 = nums[i] + nums[j]
                if sum_2 in dic:
                    dic[sum_2].append([i, j])
                else:
                    dic[sum_2] = [[i, j]]
        result = set()
        for key in dic:
            value = target - key
            if value in dic:
                list_1, list_2 = dic[key], dic[value]
                for [a, b] in list_1:
                    for [c, d] in list_2:
                        if a != c and a != d and b != c and b != d:
                            tmp = [nums[a], nums[b], nums[c], nums[d]]
                            tmp.sort()
                            result.add(tuple(tmp))
        return list(result)