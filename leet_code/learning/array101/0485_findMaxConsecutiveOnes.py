class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0 
        result = 0 

        for i in range(0, n): 
            if (nums[i] == 0): 
                count = 0
            else: 
                count+= 1 
                result = max(result, count)  

        return result 