from typing import List
from utils.mock_unit_test import mock_unit_test


class Solution:
    """
    => Link = https://leetcode.com/problems/contains-duplicate/description/

    => Technique = hash-map
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)
    

if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "nums": [
                [1,2,3,1],
                [1, 2, 3, 4],
                [1, 2, 3, 1, 2]
            ]        
        }, 
        outputs_expected= [
            True,
            False,
            True
        ],
        function=solution.containsDuplicate
    )