from typing import List
from utils.mock_unit_test import mock_unit_test


class Solution:
    """
    => Link = https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    => Technique = two-pointers
    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        Ex: input = [1,5,3,6,4]
            l_buy_idx = 1
            r_sell_idx = 5
            profit = 4

            l_buy_idx = 1
            r_sell_idx = 6
            profit = 5
        """
        l_buy_idx = 0
        max_profit = 0

        for r_sell_idx, p in enumerate(prices):
            if r_sell_idx == 0: continue

            if prices[l_buy_idx] < prices[r_sell_idx]:
                profit: int = prices[r_sell_idx] - prices[l_buy_idx]
                max_profit = max(profit, max_profit)
            else:
                l_buy_idx = r_sell_idx
        
        return max_profit

if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "prices": [
                [7,1,5,3,6,4],
                [7,6,4,3,1],
                [4, 3, 5, 2, 4, 6, 8],
                [4, 3, 5, 2, 1]
            ]        
        }, 
        outputs_expected= [
            5, 
            0,
            6,
            2
        ],
        function=solution.maxProfit
    )