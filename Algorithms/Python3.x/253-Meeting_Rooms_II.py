# lintcode link: https://www.lintcode.com/problem/meeting-rooms-ii/description
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if len(intervals) == 0: return 0
        tmp = []
        for inter in intervals:  # 标记起始点和终点
            tmp.append((inter.start, True))
            tmp.append((inter.end, False))
        tmp = sorted(tmp, key=lambda v: (v[0], v[1]))  # 排序
        n, max_num = 0, 0
        for line in tmp:  # 依次遍历每个点，遇到起始点+1，遇到终止点-1
            n = n + 1 if line[1] else n - 1
            max_num = max(n, max_num)  # 更新记录最大值
        return max_num


'''
将所有的区间在x轴上画出来，并用y轴从左到右扫描x轴，与扫描线焦点y轴的最大值就是所求
'''
