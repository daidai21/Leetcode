class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for a2 in arr2:
            for idx, a1 in enumerate(arr1):
                if a2 == a1:
                    res.append(a1)
                    arr1[idx] = None
        tmp = []
        for a1 in arr1:
            if a1 is not None:
                tmp.append(a1)
        tmp.sort()
        return res + tmp