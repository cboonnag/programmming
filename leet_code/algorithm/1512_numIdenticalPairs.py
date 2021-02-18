class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        ls_num = [0]*101
        
        for i in range(0,n):
            ls_num[ nums[i] ] += 1
        
        res = 0
        
        for i in range(0,100):
            m = ls_num[i]
            if m > 1:
                res += m*(m-1)//2
        
        return res