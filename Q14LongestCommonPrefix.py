class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        commonPrefix = ''
        if len(strs) == 0:
            return ''
        length = len(strs[0])
        for i in range(length):
            c = strs[0][i]
            for j in range(len(strs)):
                if  i >= len(strs [j]) or strs[j][i] != c:
                    return commonPrefix
            commonPrefix = commonPrefix + c
        return commonPrefix


if __name__ == '__main__':
    print(Solution.longestCommonPrefix(Solution, [""]))