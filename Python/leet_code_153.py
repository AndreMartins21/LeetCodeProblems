from typing import List
from utils.mock_unit_test import mock_unit_test


URL = "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/"


class Solution:
    def findMin(self, nums: List[int]) -> int:
        assert len(nums) == len(set(nums))
        
        result: int = nums[0]
        idx_l = 0
        idx_r = len(nums) - 1

        while idx_l <= idx_r:
            if nums[idx_l] < nums[idx_r]:
                result = min(result, nums[idx_l])
                break
                
            idx_c: int = (idx_l+idx_r) // 2
            result = min(result, nums[idx_c])
            
            if nums[idx_c] > nums[idx_l]:
                # [3, 4, 5, 1, 2] => [1, 2] 
                idx_l = idx_c + 1 
            else:
                # [5, 1, 2, 3, 4] => [5, 1]
                idx_r = idx_c - 1 
        
        return result
        

if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "nums": [
                [2,1],
                [3,4,5,1,2],
                [4,5,6,7,0,1,2],
                [11,13,15,17]                
            ]        
        }, 
        outputs_expected= [
            1,
            1,
            0,
            11
        ],
        function=solution.findMin
    )