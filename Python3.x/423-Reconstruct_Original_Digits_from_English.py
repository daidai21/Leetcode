# Runtime: 112 ms, faster than 26.92% of Python3 online submissions for Reconstruct Original Digits from English.
# Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Reconstruct Original Digits from English.
class Solution:
    def originalDigits(self, s: str) -> str:
        letters = [0] * 26  # a~z
        numbers = [0] * 10  # 0~9
        for c in s:
            letters[ord(c) - 97] += 1
        numbers[8] = letters[ord('g') - 97]
        numbers[6] = letters[ord('x') - 97]
        numbers[4] = letters[ord('u') - 97]
        numbers[2] = letters[ord('w') - 97]
        numbers[0] = letters[ord('z') - 97]
        numbers[5] = letters[ord('f') - 97] - numbers[4]
        numbers[3] = letters[ord('h') - 97] - numbers[8]
        numbers[7] = letters[ord('s') - 97] - numbers[6]
        numbers[1] = letters[ord('o') - 97] - numbers[0] - numbers[2] - numbers[4]
        numbers[9] = letters[ord('i') - 97] - numbers[5] - numbers[6] - numbers[8]
        result = ""
        for i in range(10):
            while numbers[i] > 0:
                result += str(i)
                numbers[i] -= 1
        return result
