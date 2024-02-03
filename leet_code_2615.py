from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        if len(nums) == len(set(nums)):
            return [0]*len(nums)
        
        output = []
        for i, v in enumerate(nums):
            distance = 0
            for i2, v2 in enumerate(nums):
                if (i == i2): continue

                if (v == v2):
                    distance += self.calc_distance(i, i2)
            output.append(distance)
        return output
        
    @staticmethod
    def calc_distance(x1: int, x2: int) -> int:
        return abs(x1-x2)
    

if __name__ == "__main__":
    print(
        Solution().distance(
            nums=[0, 5, 3]
        )
    )