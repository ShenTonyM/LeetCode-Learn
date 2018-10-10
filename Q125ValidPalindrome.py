class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()

        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not s[start].isalpha():
                start += 1
            while start < end and not s[end].isalpha():
                end -= 1
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True



if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))