from collections import Counter, defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (not s1) or (not s2):
            return False

        c1 = Counter(s1)
        curr_counter = c1
        length = len(s1)

        for i in range(len(s2)):
            letter = s2[i]
            if curr_counter[letter] > 0:
                curr_counter[letter] -= 1
                length -= 1
                if length == 0:
                    return True
            else:
                curr_counter[letter] -= 1

            start = i - len(s1) + 1
            if start >= 0:
                curr_counter[s2[start]] += 1

                if curr_counter[s2[start]] > 0:
                    length += 1

        return False




if __name__ == "__main__":
    print(Solution().checkInclusion("abc", "ccccbbbbaaaa"))