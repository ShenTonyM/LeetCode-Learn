class Solution1:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        lookup = dict()
        candidates = set()
        for index, item in enumerate(s):
            try:
                if lookup[item]:
                    candidates.discard(lookup[item])

            except:
                lookup[item] = index + 1
                candidates.add(index + 1)

        if len(candidates) == 0:
            return -1
        else:
            return min(candidates) - 1

if __name__ == "__main__":
    s = "aadadaad"
    print(Solution1().firstUniqChar(s))