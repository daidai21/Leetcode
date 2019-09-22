# Runtime: 184 ms, faster than 62.16% of Python3 online submissions for Find Words That Can Be Formed by Characters.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Find Words That Can Be Formed by Characters.
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for word in words:
            included = True
            chars_list = list(chars)
            for ch in word:
                if ch in chars_list:
                    chars_list.remove(ch)
                else:
                    included = False
                    break
            if included:
                result += len(word)
        return result
