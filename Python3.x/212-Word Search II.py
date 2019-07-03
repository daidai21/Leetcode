# Runtime: 336 ms, faster than 71.60% of Python3 online submissions for Word Search II.
# Memory Usage: 27.5 MB, less than 76.15% of Python3 online submissions for Word Search II.
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}  # 单词查找树
        for word in words:
            t = trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t['#'] = '#'
        self.res = set()
        self.used = [[False] * len(board[0]) for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.find(board, row, col, trie, '')
        return list(self.res)

    def find(self, board, row, col, trie, pre):
        if '#' in trie:
            self.res.add(pre)
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return 
        if not self.used[row][col] and board[row][col] in trie:
            self.used[row][col] = True
            self.find(board, row + 1, col, trie[board[row][col]], pre + board[row][col])
            self.find(board, row - 1, col, trie[board[row][col]], pre + board[row][col])
            self.find(board, row, col + 1, trie[board[row][col]], pre + board[row][col])
            self.find(board, row, col - 1, trie[board[row][col]], pre + board[row][col])
            self.used[row][col] = False
