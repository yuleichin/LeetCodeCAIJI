# -*- coding: utf-8 -*
class Solution(object):
    # 采取one-pass方式 主要找到最小值和最大值的位置，产生最大利益
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        total = len(prices)
        differ = 0
        for i in range(total-1):
            prices_buy = prices[i]
            prices_sell = prices[i+1:total]
            max_prices_sell = max(prices_sell)
            diff = max_prices_sell - prices_buy
            if diff > differ:
                differ = diff
        return differ
        """
        min_prices = 2 ** 32 - 1
        max_profit = 0
        total = len(prices)
        for i in range(total):
            if prices[i] < min_prices:
                min_prices = prices[i]
            elif prices[i] - min_prices > max_profit:
                max_profit = prices[i] - min_prices
        return max_profit
        # One Pass Algorithm, minimum valley and Maximum value, results in maxProfit

prices = [7,1,5,3,6,4]
C = Solution()
print C.maxProfit(prices)