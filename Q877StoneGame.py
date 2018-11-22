class Solution1(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True


class Solution2(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        stone_num = len(piles)

        # dp[i][j] represents how much the starting player wins
        dp = [[[] for i in range(stone_num)] for j in range(stone_num)]
        for i in range(stone_num):
            dp[i][i] = piles[i]

        for k in range(1, stone_num):
            i, j = 0, k
            while j != stone_num:
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
                i += 1
                j += 1

        if dp[0][stone_num - 1] > 0:
            return True
        else:
            return False




if __name__ == '__main__':
    print(Solution2().stoneGame([5,3,4,5]))