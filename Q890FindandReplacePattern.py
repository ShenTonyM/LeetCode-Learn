class Solution(object):

    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        result = []
        for word in words:
            if len(word) != len(pattern):
                continue

            lookup = {}
            flag = True
            for i in range(len(pattern)):
                if lookup.setdefault(pattern[i], word[i]) != word[i]:
                    flag = False
                    continue
            if len(set(lookup.values())) != len(lookup.values()):
                flag = False
                continue
            if flag:
                result.append(word)


        return result





if __name__ == "__main__":
    print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))

