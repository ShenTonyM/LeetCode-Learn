class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        lookup = dict()
        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]
            if ch1 in lookup:
                if lookup[ch1] != ch2:
                    return False
            else:
                lookup[ch1] = ch2

        if len(lookup.values()) != len(set(lookup.values())):
            return False

        return True


if __name__ == '__main__':
    print(Solution().isIsomorphic("ab", "aa"))