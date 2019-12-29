class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stk = [start]  # cur idx
        res = False
        len_arr = len(arr)
        visited = set([start])
        while stk:
            cur = stk.pop()
            if arr[cur] == 0:
                res = True
                break
            next_idx1 = cur + arr[cur]
            next_idx2 = cur - arr[cur]
            if 0 <= next_idx1 < len_arr and next_idx1 not in visited:
                stk.append(next_idx1)
                visited.add(next_idx1)
            if 0 <= next_idx2 < len_arr and next_idx2 not in visited:
                stk.append(next_idx2)
                visited.add(next_idx2)
        return res
