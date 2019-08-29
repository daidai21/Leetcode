# Runtime: 96 ms, faster than 89.20% of Python3 online submissions for Find Duplicate File in System.
# Memory Usage: 23.3 MB, less than 36.36% of Python3 online submissions for Find Duplicate File in System.
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)  # key: content, value: file path
        for path in paths:
            temp = path.split(" ")
            p = temp[0]
            for content in temp[1:]:
                name, con = content.split("(")
                dic[con].append(p + '/' + name)
        result = []
        for key in dic:
            if len(dic[key]) > 1:
                result.append(dic[key])
        return result


# Runtime: 104 ms, faster than 57.73% of Python3 online submissions for Find Duplicate File in System.
# Memory Usage: 23.6 MB, less than 36.36% of Python3 online submissions for Find Duplicate File in System.
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)  # key: content, value: file path
        for line in paths:
            data = line.split()
            root = data[0]
            for file in data[1:]:
                name, content = file.split('(')
                dic[content].append(root + '/' + name)
        return [v for v in dic.values() if len(v) > 1]
