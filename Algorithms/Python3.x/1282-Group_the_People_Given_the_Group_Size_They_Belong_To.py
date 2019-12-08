class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        temp = {}
        for idx, val in enumerate(groupSizes):
            if val in temp:
                temp[val].append(idx)
            else:
                temp[val] = [idx]
        result = []
        for val, lst in temp.items():
            for i in range(0, len(lst), val):
                result.append(lst[i:i + val])
        return result
