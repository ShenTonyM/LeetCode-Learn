from collections import defaultdict


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = defaultdict(int)

        if len(s) != len(t):
            return False

        for letter in s:
            s_dict[letter] += 1

        for letter in t:
            s_dict[letter] -= 1
            if s_dict[letter] < 0:
                return False

        return True

if __name__ == "__main__":
    s = 'anagram'
    t = 'nagaram'
    print(Solution().isAnagram(s, t))