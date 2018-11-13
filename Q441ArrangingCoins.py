class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        level = 1

        while n >= level:
            n -= level
            level += 1

        return level - 1


if __name__ == '__main__':
    print(Solution().arrangeCoins(8))