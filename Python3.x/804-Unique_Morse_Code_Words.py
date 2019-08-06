# Runtime: 36 ms, faster than 96.30% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 13.8 MB, less than 5.69% of Python3 online submissions for Unique Morse Code Words.
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        memory = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = 0
        changed_words = []
        for word in words:
            changed_word = ""
            for ch in word:
                changed_word += memory[ord(ch) - 97]
            changed_words.append(changed_word)
        return len(set(changed_words))


# Runtime: 40 ms, faster than 81.20% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 13.8 MB, less than 5.69% of Python3 online submissions for Unique Morse Code Words.
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        memory = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len(set("".join(memory[ord(ch) - ord('a')] for ch in word) for word in words))
