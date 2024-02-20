from typing import List
from utils.mock_unit_test import mock_unit_test


URL = "https://leetcode.com/problems/product-of-array-except-self/"

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_nums_return: List[int] = [1]*len(nums)
        
        prefix = 1
        for idx, n in enumerate(nums):
            list_nums_return[idx] = prefix
            prefix *= n
        
        postfix = 1
        for idx in range(len(nums)-1, -1, -1):
            list_nums_return[idx] *= postfix
            postfix *= nums[idx]
        
        return list_nums_return
            

if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "nums": [
                [1,2,3,4],
                [-1,1,0,-3,3]
            ]        
        }, 
        outputs_expected= [
            [24,12,8,6],
            [0,0,9,0,0]
        ],
        function=solution.productExceptSelf,
        order_list_output=True
    )