# Runtime: 52 ms, faster than 18.62% of Python3 online submissions for Filling Bookcase Shelves.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Filling Bookcase Shelves.
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        len_books = len(books)
        dp = [0] + [float("inf") for _ in range(len_books)]
        for i in range(1, len_books + 1):
            max_width, max_height = shelf_width, 0
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1
        return dp[-1]

