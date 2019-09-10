# Heuristics
# Runtime: 108 ms, faster than 21.29% of Python3 online submissions for Guess the Word.
# Memory Usage: 13.6 MB, less than 8.33% of Python3 online submissions for Guess the Word.
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = 0
        while n < 6:
            count = collections.Counter(w1
                    for w1 in wordlist
                        for w2 in wordlist
                            if w1 != w2 and self.match(w1, w2) == 0
            )
            guess = min(wordlist, key=lambda w: count[w])
            n = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == n]

    def match(self, word1, word2):
        matches = 0
        for ch1, ch2 in zip(word1, word2):
            matches += ch1 == ch2
        return matches
