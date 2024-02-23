from typing import List
from utils.mock_unit_test import mock_unit_test


URL = "https://leetcode.com/problems/maximum-product-subarray/description/"


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 
        max_v, min_v = 1, 1
        response = max(nums)

        for n in nums:
            if n == 0:
                min_v, max_v = 1, 1
                continue
            
            aux_max = max_v*n
            max_v = max(aux_max, min_v*n, n)           
            min_v = min(aux_max, min_v*n, n)
            
            response = max(max_v, response)

        return response            

if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "nums": [
                [2,3,-2,4],
                [1],
                [-2, 0, -1],
                [-1, -2, -3, -5, 0, 29]
            ]        
        }, 
        outputs_expected= [
            6,
            1,
            0,
            30
        ],
        function=solution.maxProduct
    )