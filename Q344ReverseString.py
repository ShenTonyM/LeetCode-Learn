class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s[::-1]
        return s

if __name__ == "__main__":
    s = "hello"
    print(Solution().reverseString(s))