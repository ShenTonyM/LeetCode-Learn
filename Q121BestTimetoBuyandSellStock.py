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


class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float('inf')
        max_profit = float('-inf')

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)

        return max_profit



if __name__ == '__main__':
    print(Solution2().maxProfit([7,1,5,3,6,4]))