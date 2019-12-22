# Time Limit Exceeded
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        sum_min = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A) + 1):
                sum_min += min(A[i:j])
        return sum_min % (10 ** 9 + 7)


# Time Limit Exceeded
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        sum_min = 0
        for i in range(len(A)):
            min_val = A[i]
            for j in range(i, len(A)):
                min_val = min(min_val, A[j])
                sum_min += min_val
        return sum_min % (10 ** 9 + 7)


# DP
# Runtime: 644 ms, faster than 16.52% of Python3 online submissions for Sum of Subarray Minimums.
# Memory Usage: 17.7 MB, less than 8.33% of Python3 online submissions for Sum of Subarray Minimums.
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        left, right = [0] * len(A), [0] * len(A)
        # left -> right
        stk = []
        for i in range(len(A)):
            cnt = 1
            while stk and stk[-1][0] > A[i]:
                cnt += stk.pop()[1]
            left[i] = cnt
            stk.append((A[i], cnt))
        # right -> left
        stk = []
        for i in range(len(A) - 1, -1, -1):
            cnt = 1
            while stk and stk[-1][0] >= A[i]:
                cnt += stk.pop()[1]
            right[i] = cnt
            stk.append((A[i], cnt))
        # left * right * A
        return sum([a * l * r for (a, l, r) in zip(A, left, right)]) % (10 ** 9 + 7)
