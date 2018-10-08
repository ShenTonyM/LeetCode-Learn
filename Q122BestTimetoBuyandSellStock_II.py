class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        accumulationProfit = 0
        buy = 10000
        sell = -10000
        prev_price = 5000

        for price in prices:
            # 卖上次，买这次
            if price < prev_price:
                sell = prev_price
                profit = sell - buy
                if profit > 0:
                    accumulationProfit += profit
                buy = price
                sell = -10000
                prev_price = price
            # 不动
            else:
                prev_price = price

        # 最后一次抛掉
        if prev_price > buy:
            profit = prev_price - buy
            accumulationProfit += profit
        return accumulationProfit


if __name__ == '__main__':
    print(Solution().maxProfit([7,6,4,3,1]))