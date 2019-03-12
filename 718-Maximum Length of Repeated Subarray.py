# dp
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        result = 0
        length_a, length_b = len(A), len(B)
        dp = [[0 for _ in range(length_a)] for _ in range(length_b)]
        for a in range(length_a):  # initialize
            if A[a] == B[0]: dp[0][a] = 1
        for b in range(length_b):  # initialize
            if B[b] == A[0]: dp[b][0] = 1
        for a in range(1, length_a):  # state trainsition
            for b in range(1, length_b):
                if A[a] == B[b]:
                    dp[b][a] += 1 + dp[b - 1][a - 1]  # state trainsition equation
        for row in dp:  # find max of matrix named dp
            result = max(result, max(row))
        return result


# violence
# Time Limit Exceeded
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        result = 0
        length_a, length_b = len(A), len(B)
        for a in range(length_a):
            for b in range(length_b):
                if A[a] == B[b]:
                    same_num = 1
                    tmp_a, tmp_b = a + 1, b + 1
                    while tmp_a < length_a and tmp_b < length_b:
                        if A[tmp_a] == B[tmp_b]:
                            same_num += 1
                            tmp_a += 1
                            tmp_b += 1
                        else:
                            break
                    result = max(result, same_num)
        return result
