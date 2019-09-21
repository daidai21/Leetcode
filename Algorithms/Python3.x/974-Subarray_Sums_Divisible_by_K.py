# Time Limit Exceeded
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        result = 0
        for i in range(len(A) + 1):
            for j in range(i + 1, len(A) + 1):
                result += sum(A[i:j]) % K == 0
        return result


# Time Limit Exceeded
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        result = 0
        pre_list = [0] * (len(A) + 1)
        for i in range(len(A)):
            pre_list[i + 1] = pre_list[i] + A[i]
        for i in range(len(A) + 1):
            for j in range(i + 1, len(A) + 1):
                result += (pre_list[j] - pre_list[i]) % K == 0
        return result


# Runtime: 328 ms, faster than 97.99% of Python3 online submissions for Subarray Sums Divisible by K.
# Memory Usage: 17.9 MB, less than 10.00% of Python3 online submissions for Subarray Sums Divisible by K.
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        result = 0
        prefix = 0
        count = [1] + [0] * K
        for a in A:
            prefix = (prefix + a) % K
            result += count[prefix]
            count[prefix] += 1
        return result


"""
if a % c = b % c, so (a - b) % c = 0
"""
