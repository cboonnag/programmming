class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        
        run = 0
        i = 0
        while i < n:
            run += nums[i]
            res.append(run)
            i += 1 
            
        return res