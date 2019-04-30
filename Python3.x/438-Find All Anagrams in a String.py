# dict
class Solution:
    def findAnagrams(self, s: 'str', p: 'str') -> 'List[int]':
        if len(s) < len(p): return []
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        map_a = {c:0 for c in alphabets}
        map_p = {c:0 for c in alphabets}
        res = []
        for i, c in enumerate(p):
            map_p[c] += 1
            if i < len(p) - 1: map_a[s[i]] += 1
        lead, lag = len(p) - 1, 0
        while lead < len(s):
            map_a[s[lead]] += 1
            if map_a == map_p: res.append(lag)
            map_a[s[lag]] -= 1
            lead, lag = lead + 1, lag + 1
        return res
