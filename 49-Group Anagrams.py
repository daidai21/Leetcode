class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        dict, result, n = {}, [], 0
        for item in strs:
            standard = tuple(sorted(item))
            idx = dict.get(standard)
            if idx is None:
                dict[standard] = n
                result.append([item])
                n += 1
            else:
                result[idx].append(item)
        return result


'''
使用sorted保证同组内会是同样的flag
dict的value存储的是对应key的组的大小
result直接访问idx
'''
