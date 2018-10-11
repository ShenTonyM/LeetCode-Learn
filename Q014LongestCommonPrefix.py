class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        length = len(strs[0])
        for i in range(length):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))