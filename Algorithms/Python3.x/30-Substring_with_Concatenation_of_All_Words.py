# Runtime: 72 ms, faster than 82.84% of Python3 online submissions for Substring with Concatenation of All Words.
# Memory Usage: 13.4 MB, less than 35.78% of Python3 online submissions for Substring with Concatenation of All Words.
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s == '' or len(words) == 0 or len(words[0]) * len(words) > len(s):
            return []
        self.res, self.len_word, self.len_words, self.len_s = [], len(words[0]), len(words), len(s)
        self.dict_words = {}
        for word in words:
            self.dict_words[word] = self.dict_words[word] + 1 if word in self.dict_words else 1
        for i in range(min(self.len_word, self.len_s - self.len_words * self.len_word + 1)):
            self.helper(i, i, s)
        return self.res

    def helper(self, l, r, s):
        cur = {}
        while r + self.len_word <= self.len_s:
            w = s[r:r + self.len_word]
            r += self.len_word
            if w not in self.dict_words:
                l = r
                cur.clear()
            else:
                cur[w] = cur[w] + 1 if w in cur else 1
                while cur[w] > self.dict_words[w]:
                    cur[s[l:l + self.len_word]] -= 1
                    l += self.len_word
                if r - l == self.len_word * self.len_words:
                    self.res.append(l)
