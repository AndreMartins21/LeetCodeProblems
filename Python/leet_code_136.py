from typing import List
from utils.mock_unit_test import mock_unit_test


URL = "https://leetcode.com/problems/single-number/"


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        To solve this problem, I employed the concept of bitwise XOR operation between two numbers. In brief, this operation involves:
        Comparing each bit of both numbers, and
        If both bits are equal (either both are 1 or both are 0), it returns 0; 
        otherwise, it returns 1.

        time: O(n)
        space: O(1)
        """
        aux = 0

        for n in nums:
            aux ^= n
        return aux            
            

if __name__ == "__main__":
    solution = Solution()

    mock_unit_test(
        dict_inputs_tests= {
            "nums": [
                [2, 2, 1],
                [4, 1, 2, 1, 2],
                [2]
            ]        
        }, 
        outputs_expected= [
            1,
            4,
            2
        ],
        function=solution.singleNumber
    )