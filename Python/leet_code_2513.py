class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        list1 = []
        num = 1
        while (len(list1) < uniqueCnt1):
            if self.is_not_divisible(num, divisor1):
                list1.append(num)
            num += 1
        

        list2 = []
        num = 1
        while (len(list2) < uniqueCnt2):
            if self.is_not_divisible(num, divisor2) and num not in list1:
                list2.append(num)
            num += 1
        
        return max(
            list1+list2
        )
    
    @staticmethod
    def is_not_divisible(x: int, divisor: int):
        return x % divisor != 0
    

if __name__ == "__main__":
    print(
        Solution().minimizeSet(
            divisor1 = 6
            divisor2 = 3, 
            uniqueCnt1 = 2, 
            uniqueCnt2 = 10
        )
    )