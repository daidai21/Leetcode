# Runtime: 76 ms, faster than 99.32% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 12.9 MB, less than 17.14% of Python3 online submissions for Queue Reconstruction by Height.
class Solution:
    def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
        people = sorted(people, key = lambda x: (-x[0], x[1]))  # 高度递减，k增加 排序
        result = []
        for item in people:
             result.insert(item[1], item)  # 根据k前面不低于自己身高人数 插入
        return result
