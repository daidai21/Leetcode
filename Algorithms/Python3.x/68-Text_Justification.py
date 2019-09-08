# brute force
# Runtime: 28 ms, faster than 99.33% of Python3 online submissions for Text Justification.
# Memory Usage: 14.1 MB, less than 25.00% of Python3 online submissions for Text Justification.
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        # split
        start = 0
        len_words = len(words)
        while start < len_words:
            tmp = [words[start]]
            len_tmp = len(words[start])
            while start + 1 < len_words and len_tmp + 1 + len(words[start + 1]) <= maxWidth:
                start += 1
                len_tmp += 1 + len(words[start])
                tmp.append(words[start])
                print(start + 1, len_tmp, tmp)
            result.append(tmp)
            start += 1
        # fill
        for idx, line in enumerate(result):
            len_word = 0
            for word in line:
                len_word += len(word)
            if len(line) == 1 and idx != len(result) - 1:
                new_line = line[0] + (maxWidth - len(line[0])) * ' '
            elif idx == len(result) - 1:  # end line
                new_line = ' '.join(line)
                for _ in range(len(new_line), maxWidth):
                    new_line += ' '
            elif len_word + len(line) - 1 < maxWidth:  # fill not equal space
                add_space = (maxWidth - (len_word + len(line) - 1)) // (len(line) - 1)  # add space num for every word
                add_space_end = (maxWidth - (len_word + len(line) - 1)) % (len(line) - 1)  # add extra space in 0~add_space_end index
                for i, word in enumerate(line):
                    if i == len(line) - 1:
                        pass
                    elif i < add_space_end:
                        line[i] += add_space * ' ' + ' '
                    else:
                        line[i] += add_space * ' '
                new_line = ' '.join(line)
            elif len_word + len(line) - 1 == maxWidth:  # fill one space
                new_line = ' '.join(line)
            result[idx] = new_line
        return result
