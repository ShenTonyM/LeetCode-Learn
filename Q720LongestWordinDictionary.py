class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        sort_words = sorted(words, key=lambda x:(len(x),x))
        print(sort_words)

        candidates = set()

        for word in sort_words:
            if len(word) == 1:
                candidates.add(word)
            else:
                if word[:-1] in candidates:
                    candidates.add(word)

        candidates = sorted(list(candidates), key=lambda x:[len(x),x])[::-1]

        longest_length = len(candidates[0])
        result = candidates[0]
        for word in candidates[1:]:
            if len(word) == longest_length:
                result = word
            else:
                return result

        return result


if __name__ == '__main__':
    print(Solution().longestWord(["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]))