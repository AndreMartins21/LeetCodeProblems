from typing import List
from utils.mock_unit_test import mock_unit_test


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [0, 1]



if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "nums": [
                [2,7,11,15],
                [3, 2, 4], 
                [3, 3]
            ],
            "target": [
                9,
                6,
                6
            ]
            
        }, 
        outputs_expected= [
            [0, 1],
            [1, 2],
            [0, 1]
        ],
        function=solution.twoSum
    )