from collections import deque
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        digits = deque()
        while x != 0:
            digit = x % 10
            digits.append(digit)
            x = x // 10

        while len(digits) > 1:
            n1 = digits.popleft()
            n2 = digits.pop()
            if n1 != n2:
                return False

        return True

if __name__ == "__main__":
    print(Solution.isPalindrome(Solution,1534236469))