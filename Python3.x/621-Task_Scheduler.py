# formula method
# Runtime: 64 ms, faster than 79.65% of Python3 online submissions for Task Scheduler.
# Memory Usage: 13.3 MB, less than 5.03% of Python3 online submissions for Task Scheduler.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        most = count.most_common()[0][1]
        num_most = len([i for i, v in count.items() if v == most])
        time = (most - 1) * (n + 1) + num_most
        return max(time, len(tasks))


'''
（最多任务数-1）*（n + 1） + （相同最多任务的任务个数）
'''
