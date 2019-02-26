class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        curr_char_index = 0

        for i in range(len(t)):
            if s[curr_char_index] == t[i]:
                if curr_char_index == len(s) - 1:
                    return True
                else:
                    curr_char_index += 1

        return False


if __name__ == '__main__':
    print(Solution().isSubsequence("axc", "ahbgdc"))