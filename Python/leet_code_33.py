from typing import List
from utils.mock_unit_test import mock_unit_test


URL = "https://leetcode.com/problems/search-in-rotated-sorted-array/description/"


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        assert len(nums) == len(set(nums))
        
        idx_result: int = 0
        idx_l = 0
        idx_r = len(nums) - 1

        while idx_l <= idx_r:
            idx_c = (idx_l + idx_r) // 2
            
            if nums[idx_c] == target:
                return idx_c
                
            # [5, 1, 3], target = 5
            # portion left:
            if nums[idx_l] <= nums[idx_c]:
                if target > nums[idx_c] or target < nums[idx_l]:
                    idx_l = idx_c + 1
                else:
                    idx_r = idx_c - 1
            # portion right
            else:
                if target < nums[idx_c] or target > nums[idx_r]:
                    idx_r = idx_c - 1 
                else:
                    idx_l = idx_c + 1
        
        return -1


if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "nums": [
                # [4,5,6,7,0,1,2],
                # [4,5,6,7,0,1,2],
                # [1],
                [5,1,3]
            ],
            "target": [
                # 0,
                # 3,
                # 0,
                5
            ]        
        }, 
        outputs_expected= [
            # 4,
            # -1,
            # -1,
            0
        ],
        function=solution.search
    )