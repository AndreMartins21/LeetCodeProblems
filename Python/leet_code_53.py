from typing import List
from utils.mock_unit_test import mock_unit_test


URL = "https://leetcode.com/problems/maximum-subarray/"


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = float('-inf')
        cur_sum = 0
        
        for n in nums:
            cur_sum = 0 if cur_sum < 0 else cur_sum
            
            cur_sum += n
            max_sub = max(cur_sum, max_sub)

        return max_sub                


if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "nums": [
                [-2,1,-3,4,-1,2,1,-5,4],
                [1],
                [5,4,-1,7,8]
            ]        
        }, 
        outputs_expected= [
            6,
            1,
            23
        ],
        function=solution.maxSubArray
    )