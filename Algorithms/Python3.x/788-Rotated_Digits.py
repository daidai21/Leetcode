# using string
class Solution:
    def rotatedDigits(self, N: int) -> int:
        counts = 0
        for num in range(1, N + 1):
            number = str(num)
            if '3' in number or '7' in number or '4' in number:  # this will be an invalid number upon rotation
                continue  # skip this number and go to next itertaion
            if '2' in number or '5' in number or '6' in number or '9' in number:
                counts += 1
        return counts  # return result


# optimize
class Solution:
    def rotatedDigits(self, N: int) -> int:
        counts = 0
        for num in range(1, N + 1):
            number = str(num)
            if '3' in number or '7' in number or '4' in number: continue
            if '2' in number or '5' in number or '6' in number or '9' in number: counts += 1
        return counts


# optimize
class Solution:
    def rotatedDigits(self, N: int) -> int:
        counts = 0
        for num in range(1, N + 1):
            if '3' in str(num) or '7' in str(num) or '4' in str(num): continue
            if '2' in str(num) or '5' in str(num) or '6' in str(num) or '9' in str(num): counts += 1
        return counts
