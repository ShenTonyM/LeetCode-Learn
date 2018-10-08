class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        bestProfit = 0
        buy = 10000
        sell = -10000

        for price in prices:
            if price < buy:
                if sell > buy:
                    profit = sell - buy
                    if profit > bestProfit:
                        bestProfit = profit
                buy = price
                sell = -10000

            elif price > sell:
                sell = price

        if sell > buy:
            profit = sell - buy
            if profit > bestProfit:
                bestProfit = profit
        return bestProfit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))