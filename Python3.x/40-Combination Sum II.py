# Runtime: 760 ms, faster than 6.44% of Python3 online submissions for Combination Sum II.
# Memory Usage: 14.1 MB, less than 5.41% of Python3 online submissions for Combination Sum II.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, candidates = [], sorted(candidates)
        def recursion(idx, target, curr):
            if target < 0:
                return
            elif target == 0:
                if curr not in res:
                    res.append(curr)
            else:
                if idx >= len(candidates):
                    return
                else:
                    recursion(idx + 1, target, curr)
                    recursion(idx + 1, target - candidates[idx], curr + [candidates[idx]])

        recursion(0, target, [])
        return sorted(res)