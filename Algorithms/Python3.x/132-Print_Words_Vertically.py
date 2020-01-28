from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        len_row = s.count(' ') + 1
        len_col = max([len(word) for word in s.split(' ')])
        mat = [[' '] * len_col for _ in range(len_row)]
        words = s.split(' ')
        for row in range(len_row):
            for col in range(len_col):
                if col < len(words[row]):
                    mat[row][col] = words[row][col]
        res = []
        for col in range(len_col):
            word = ""
            for row in range(len_row):
                word += mat[row][col]
            res.append(word.rstrip())
        return res


print(Solution().printVertically("HOW ARE YOU"))  # ["HAY","ORO","WEU"]
print(Solution().printVertically("TO BE OR NOT TO BE"))
print(Solution().printVertically("CONTEST IS COMING"))
