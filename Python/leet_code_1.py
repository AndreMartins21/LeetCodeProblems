from typing import List
from utils.mock_unit_test import mock_unit_test


class Solution:
    # Link = https://leetcode.com/problems/two-sum/description/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map: dict = {}

        for idx, n in enumerate(nums):
            difference: int = target - n
            
            if difference in hash_map.keys():
                return [idx, hash_map.get(difference)]
            hash_map[n] = idx
        return []


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
        function=solution.twoSum,
        order_list_output=True
    )