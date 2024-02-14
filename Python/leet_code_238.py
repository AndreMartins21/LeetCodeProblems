from typing import List

URL = "https://leetcode.com/problems/product-of-array-except-self/"

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_nums_return: List[int] = []
        len_num = len(nums)

        for i in range(len_num):
            if (i == 0):
                values = nums[1:]
            elif (i == len_num -1):
                values = nums[:-1]
            else:
                values = nums[:i] + nums[i+1:]
            
            list_nums_return.append()
            