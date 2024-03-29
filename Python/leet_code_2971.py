from typing import List
from utils.mock_unit_test import mock_unit_test


class Solution:
    """
    https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/?envType=daily-question&envId=2024-02-15
    """
    def largestPerimeter(self, nums: List[int]) -> int:
        nums: List[int] = sorted(nums)
        sum_tot: int = sum(nums)
        current_sum: int = 0

        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            current_sum += n  # 5
            remaining: int = sum_tot - current_sum  # 10
            
            if nums[i] < remaining:
                return remaining + n
        return -1


if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "nums": [
                [1,12,1,2,5,50,3], 
                [5,5,50]
            ]
        }, 
        outputs_expected= [
            12,
            -1
        ],
        function=solution.largestPerimeter
    )