# 贪心
# gas:表示在该点能获得多少油
# cost:表示在从该点到下一点要耗费多少油
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, remain, debt = 0, 0, 0
        for i in range(len(gas)):
            remain += gas[i] - cost[i]
            if remain < 0:
                debt += remain
                start = i + 1
                remain = 0
        return start if remain + debt >= 0 else -1
