class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num == 0:
            return False

        factors = [2, 3, 5]

        for factor in factors:
            while num % factor == 0:
                num /= factor

        return num == 1


if __name__ == '__main__':
    print(Solution().isUgly(14))