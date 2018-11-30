# O(n^2) Exceed Time Limit
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        max_length = 0
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if len(s[i:j]) == len(set(s[i:j])):
                    if j - i > max_length:
                        max_length = j - i

        return max_length

# O(n)
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        lookup = {}
        max_length = 0

        i,j = 0, 0

        while j != len(s):
            if s[j] not in lookup:
                lookup[s[j]] = j
            else:
                # j的前一项截止
                max_length = max(max_length, j - i)
                prev_j = lookup[s[j]]
                # 前面（i, perv_j）之间元素删除
                for index in range(i, prev_j):
                    if s[index] in lookup:
                        lookup.pop(s[index])

                # 更新是s[j]
                lookup[s[j]] = j
                i = prev_j + 1

            j += 1

        return max(max_length, j - i)




if __name__ == '__main__':
    print(Solution2().lengthOfLongestSubstring(" "))