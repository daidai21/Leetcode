# Runtime: 180 ms, faster than 39.29% of Python3 online submissions for Minimum Index Sum of Two Lists.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Index Sum of Two Lists.
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_dic = {}
        idx_dic = {}
        if not list1 or not list2:
            return None
        for idx, val in enumerate(list1):
            hash_dic[val] = idx
        for i in range(len(list2)):
            if list2[i] in hash_dic:
                if hash_dic[list2[i]] + i not in idx_dic:
                    idx_dic[hash_dic[list2[i]] + i] = [list2[i]]
                else:
                    idx_dic[hash_dic[list2[i]] + i].append(list2[i])
        return idx_dic[min(idx_dic)]
