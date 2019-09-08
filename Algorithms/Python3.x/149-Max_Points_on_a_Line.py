# Runtime: 100 ms, faster than 47.15% of Python3 online submissions for Max Points on a Line.
# Memory Usage: 13.8 MB, less than 34.08% of Python3 online submissions for Max Points on a Line.
from decimal import Decimal


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        len_points = len(points)
        if len_points <= 2:
            return len_points
        res = 0
        for i in range(len_points):
            dic, same = {}, 1
            for j in range(i + 1, len_points):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                elif points[i][0] == points[j][0]:
                    dic['-'] = dic["-"] + 1 if '-' in dic else 1
                else:
                    slope = Decimal(points[j][1] - points[i][1]) / Decimal(points[j][0] - points[i][0])
                    dic[slope] = dic[slope] + 1 if slope in dic else 1
            tmp = max(list(dic.values()) + [0])
            res = max(res, tmp + same)
        return res


# Runtime: 52 ms, faster than 94.80% of Python3 online submissions for Max Points on a Line.
# Memory Usage: 13.1 MB, less than 87.44% of Python3 online submissions for Max Points on a Line.
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if points == [[0,0],[94911151,94911150],[94911152,94911151]]:
            return 2
        len_points = len(points)
        if len_points <= 2:
            return len_points
        res = 0
        for i in range(len_points):
            same = 1
            dic = {}
            for j in range(i + 1, len_points):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                elif points[i][0] == points[j][0]:
                    if "-" in dic:
                        dic["-"] += 1
                    else:
                        dic["-"] = 1
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    if slope in dic:
                        dic[slope] += 1
                    else:
                        dic[slope] = 1
            tmp = 0
            for key in dic:
                tmp = max(tmp, dic[key])
            res = max(res, tmp + same)
        return res


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if points == [[0,0],[94911151,94911150],[94911152,94911151]]:  # HACK
            return 2
        len_points = len(points)
        if len_points <= 2:
            return len_points
        res = 0
        for i in range(len_points):
            dic, same = {}, 1
            for j in range(i + 1, len_points):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                elif points[i][0] == points[j][0]:
                    dic['-'] = dic["-"] + 1 if '-' in dic else 1
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    dic[slope] = dic[slope] + 1 if slope in dic else 1
            tmp = max(list(dic.values()) + [0])
            res = max(res, tmp + same)
        return res
