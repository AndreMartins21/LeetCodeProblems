from typing import List
from utils.mock_unit_test import mock_unit_test


URL = "https://leetcode.com/problems/"


class Solution:
    def function(self, nums: List[int]) -> int:
        """
        Description here
        """
        pass
            

if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "nums": [
            ]        
        }, 
        outputs_expected= [
        ],
        function=solution.function
    )