# Runtime: 56 ms, faster than 85.88% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 14.2 MB, less than 44.77% of Python3 online submissions for Fizz Buzz.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i + 1) for i in range(n)]
        for i, _ in enumerate(res):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                res[i] = "FizzBuzz"
                continue
            if (i + 1) % 3 == 0:
                res[i] = "Fizz"
                continue
            if (i + 1) % 5 == 0:
                res[i] = "Buzz"
                continue
        return res


# Runtime: 48 ms, faster than 98.48% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 14.2 MB, less than 54.78% of Python3 online submissions for Fizz Buzz.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0: res.append("FizzBuzz")
            elif (i + 1) % 3 == 0: res.append("Fizz")
            elif (i + 1) % 5 == 0: res.append("Buzz")
            else: res.append(str(i + 1))
        return res
