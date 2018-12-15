class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        candidates = set(words)

        for word in candidates:
            for i in range(1,len(word)):
                candidates.discard(word[1:])

        return sum([len(word) for word in candidates])


if __name__ == '__main__':
    print(Solution().minimumLengthEncoding(["time", "me", "bell"]))