from typing import List


class Solution:
    def maxProfit(self, prices: List[int] ) -> int:
        profit = 0
        bp = prices[0]

        for i in range(len(prices)):
            if bp > prices[i]:
                bp = prices[i]
            else:
                profit = max(profit, prices[i] - bp)
        return profit




prices = [7,1,5,3,6,4]

obj = Solution()

print(obj.maxProfit(prices))

