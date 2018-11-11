class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if not amount:
            return 0

        coins.sort()
        table = [float("inf") for i in range(amount + 1)]
        table[0] = 0

        for coin in coins:
            for i in range(amount + 1):
                if coin + i <= amount:
                    table[coin + i] = min(table[coin + i], table[i] + 1)


        return table[amount] if table[amount] != float('inf') else -1





if __name__ == "__main__":
    print(Solution().coinChange([1, 2, 5], 11))