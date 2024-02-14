from typing import List


class Solution:
    @staticmethod
    def get_dict_with_pos_and_neg(nums: List[int]) -> dict:
        result: dict = {"pos": [], "neg": []}

        for n in nums:
            if n > 0: result["pos"].append(n)
            else: result["neg"].append(n)
        
        return result    
    
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        new_nums: List[int] = []        

        map_pos_neg: dict = self.get_dict_with_pos_and_neg(nums)
        
        for i in range(len(nums)//2):
            new_nums.append(map_pos_neg["pos"][i])
            new_nums.append(map_pos_neg["neg"][i])

        return new_nums
            
            
if __name__ == "__main__":
    solution = Solution()
    arrays = [
        [3,1,-2,-5,2,-4], [-1, 1]
    ]

    for array in arrays:
        solution.rearrangeArray(array)