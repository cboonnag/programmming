class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ls = [0]*101
        res = []
        n = len(nums)
        
        for i in range(n):
            ls[nums[i]] += 1
        
        for i in range(n):
            n_small = sum( ls[:nums[i]] )
            res.append(n_small)
            
        return res