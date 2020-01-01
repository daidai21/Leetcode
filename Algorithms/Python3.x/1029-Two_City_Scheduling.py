# greedy
# Runtime: 36 ms, faster than 89.96% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Two City Scheduling.
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda cost: cost[0] - cost[1])
        return sum([costs[i][0] + costs[i + len(costs) // 2][1] for i in range(len(costs) // 2)])
