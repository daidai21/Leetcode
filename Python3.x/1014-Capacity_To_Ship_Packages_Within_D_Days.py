# binary search
# Runtime: 836 ms, faster than 14.93% of Python3 online submissions for Capacity To Ship Packages Within D Days.
# Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Capacity To Ship Packages Within D Days.
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        smallest, largest = max(weights), sum(weights)
        while smallest < largest:  # 袋子的容量 小于 weights的和
            mid, need, tmp = (smallest + largest) / 2, 1, 0
            for weight in weights:
                if tmp + weight > mid: need, tmp = need + 1, 0
                tmp += weight
            if need > D: smallest = mid + 1  # 如果需要的袋子的数量 大于 天数，
            else: largest = mid
        return int(smallest)  # 向下取整


'''
首先确定船的容量范围：
    最小值smallest  最大的weight[i]
    最大值largest  所有weight[i]的和
然后使用二分搜索在[smallest, largest]中寻找合适的容量
'''
